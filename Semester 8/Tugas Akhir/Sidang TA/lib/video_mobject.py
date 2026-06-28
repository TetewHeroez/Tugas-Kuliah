from manim import *
import cv2
import numpy as np
from PIL import Image
from dataclasses import dataclass

@dataclass
class VideoStatus:
    time: float = 0
    # Kita hapus tipe data eksplisit cv2 di sini biar pickle gak bingung
    videoObject: object = None 
    
    def __deepcopy__(self, memo):
        return self

class VideoMobject(ImageMobject):
    '''
    Modified VideoMobject with Cache Support.
    Excludes cv2 object from pickling to prevent cache misses.
    '''
    def __init__(self, filename=None, imageops=None, speed=1.0, loop=False, **kwargs):
        self.filename = filename
        self.imageops = imageops
        self.speed    = speed
        self.loop     = loop
        
        # ID dibuat dari filename. Selama nama file sama, Cache dianggap SAMA.
        self._id = str(filename) 
        
        # Setup awal
        self.init_video_capture()
        
        # Set gambar awal (thumbnail)
        img = self.get_current_frame_image()
        super().__init__(img, **kwargs)
        
        # Add updater
        self.add_updater(self.videoUpdater)

    def init_video_capture(self):
        """Fungsi helper untuk inisialisasi OpenCV"""
        self.status = VideoStatus()
        self.status.videoObject = cv2.VideoCapture(self.filename)
        self.status.videoObject.set(cv2.CAP_PROP_POS_FRAMES, 1)

    def get_current_frame_image(self):
        """Helper untuk ambil frame saat ini jadi Image"""
        if self.status.videoObject is None:
             self.init_video_capture()

        ret, frame = self.status.videoObject.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            if self.imageops:
                img = self.imageops(img)
            return img
        else:
            # Placeholder merah transparan
            return Image.fromarray(np.uint8([[63, 0, 0, 0], [0, 127, 0, 0], [0, 0, 191, 0], [0, 0, 0, 255]]))

    # --- MAGIS CACHING ADA DI SINI ---
    def __getstate__(self):
        """
        Saat Manim mau simpan Cache, fungsi ini dipanggil.
        Kita HAPUS 'status' (yang berisi objek C++ cv2) dari daftar yang disimpan.
        """
        state = self.__dict__.copy()
        if "status" in state:
            del state["status"] # Buang objek OpenCV yang bikin error pickle
        return state

    def __setstate__(self, state):
        """
        Saat Cache di-load kembali.
        Kita load variabel aman, lalu kita inisialisasi ulang OpenCV-nya manual.
        """
        self.__dict__.update(state)
        # Bikin ulang objek OpenCV karena tadi tidak disimpan
        self.init_video_capture()
    # ---------------------------------

    def videoUpdater(self, mobj, dt):
        if dt == 0:
            return
        
        # Pastikan objek video ada (jika baru load dari cache)
        if not hasattr(self, "status") or self.status.videoObject is None:
            self.init_video_capture()

        status = self.status
        status.time += 1000 * dt * mobj.speed
        
        self.status.videoObject.set(cv2.CAP_PROP_POS_MSEC, status.time)
        ret, frame = self.status.videoObject.read()
        
        # Logika Looping
        if (ret == False) and self.loop:
            status.time = 0
            self.status.videoObject.set(cv2.CAP_PROP_POS_MSEC, status.time)
            ret, frame = self.status.videoObject.read()
        
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            if mobj.imageops != None:
                img = mobj.imageops(img)
            
            mobj.pixel_array = change_to_rgba_array(
                np.asarray(img), mobj.pixel_array_dtype
            )