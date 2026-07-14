\ProvidesClass{form-TA}[2024/01/01 Template Form TA ITS]
\NeedsTeXFormat{LaTeX2e}
\LoadClass[a4paper,12pt]{article}

% -------------------------
% PACKAGES UMUM
% -------------------------
\RequirePackage[left=2cm, right=2cm, top=1.25cm, bottom=2cm]{geometry}
\RequirePackage{graphicx}
\RequirePackage{multirow}
\RequirePackage{array}
\RequirePackage{amssymb}
\RequirePackage[T1]{fontenc}
\RequirePackage{carlito}
\RequirePackage[scaled]{helvet}
\RequirePackage[table]{xcolor}
\RequirePackage{float}
\RequirePackage{hyperref}
\RequirePackage[export]{adjustbox}
\RequirePackage{newtxtext}
\RequirePackage{ifthen}
\RequirePackage[indonesian]{babel}
\RequirePackage{fancyhdr}
\RequirePackage{lastpage}
\RequirePackage{xparse}

\setlength{\headheight}{15pt}
\setlength{\footskip}{0cm}
\renewcommand{\headrulewidth}{0pt}
\graphicspath{{./}{../}}


% ================
% Pecah \today
% ================
\edef\todayday{\number\day}
\edef\todaymonth{%
    \ifcase\month
      \or Januari%
      \or Februari%
      \or Maret%
      \or April%
      \or Mei%
      \or Juni%
      \or Juli%
      \or Agustus%
      \or September%
      \or Oktober%
      \or November%
      \or Desember%
    \fi
}
\edef\todayyear{\number\year}



% Default sans serif = Helvetica
\renewcommand{\familydefault}{\sfdefault}

% Warna
\definecolor{headerblue}{RGB}{125,140,165}
\definecolor{linkblue}{RGB}{0,0,255}
\definecolor{titlegray}{RGB}{102,102,102}

\renewcommand{\arraystretch}{1.2}

\newcommand{\@judul}{Judul T.A.}
\DeclareRobustCommand{\Judul}[1]{%
    \renewcommand{\@judul}{#1}%
}

\newcommand{\@nama}{Nama Mahasiswa}
\DeclareRobustCommand{\Nama}[1]{%
   \renewcommand{\@nama}{#1}%
}

\newcommand{\@NRP}{1210100999}
\DeclareRobustCommand{\NRP}[1]{%
   \renewcommand{\@NRP}{#1}
}

\newcommand{\@pnrm}{Toat Aminullah}
\DeclareRobustCommand{\Penerima}[1]{%
   \renewcommand{\@pnrm}{#1}
}

\newcommand\@jur{Matematika}
\DeclareRobustCommand\Departemen[1]{%
   \renewcommand\@jur{#1}
}

\newcommand\@fak{Sains dan Analitika Data}
\DeclareRobustCommand\Fakultas[1]{%
   \renewcommand\@fak{#1}
}

\newcommand\@lab{Pemodelan dan Simulasi Sistem}
\DeclareRobustCommand\Laboratorium[1]{%
   \renewcommand\@lab{#1}
}

\newcommand\@tgl{\todayday}
\DeclareRobustCommand\Tanggal[1]{%
   \renewcommand\@tgl{#1}
}

\newcommand\@bulan{\todaymonth}
\DeclareRobustCommand\Bulan[1]{%
   \renewcommand\@bulan{#1}
}

\newcommand\@tahun{\todayyear}
\DeclareRobustCommand\Tahun[1]{%
   \renewcommand\@tahun{#1}
}

\newcommand\@rev{01}
\DeclareRobustCommand\Revisi[1]{%
   \renewcommand\@rev{#1}
}

\newcommand\@smt{Genap}
\DeclareRobustCommand\Semester[1]{%
   \renewcommand\@smt{#1}
}

\newcommand\@thnajr{2025/2026}
\DeclareRobustCommand\TahunAjaran[1]{%
   \renewcommand\@thnajr{#1}
}

\newcommand\@pbbsatu{Nama Pembimbing Pertama}
\newcommand\@pbbdua{Nama Pembimbing Kedua}
\DeclareRobustCommand\Pembimbing[2]{%
   \renewcommand{\@pbbsatu}{#1}%
   \renewcommand{\@pbbdua}{#2}%
}
\newcommand\@NIPpbbsatu{12345678 123456 1 123}
\newcommand\@NIPpbbdua{12345678 123456 1 123}
\DeclareRobustCommand\NIPPembimbing[2]{%
   \renewcommand{\@NIPpbbsatu}{#1}%
   \renewcommand{\@NIPpbbdua}{#2}%
}

\newcommand{\ShortPbbSatu}{%
  \expandafter\short@name\@pbbsatu\relax
}

\newcommand{\ShortPbbDua}{%
  \expandafter\short@name\@pbbdua\relax
}

\newcommand{\DaftarPembimbing}{%
  \@pbbsatu%
  \ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}{}{, \@pbbdua}%
}

\newcommand\@periodewisuda{134}
\DeclareRobustCommand\PeriodeWisuda[1]{%
   \renewcommand\@periodewisuda{#1}
}

\newcommand\@tahunwisuda{2026}
\DeclareRobustCommand\TahunWisuda[1]{%
   \renewcommand\@tahunwisuda{#1}
}

\newcommand\@kaprodi{Dr. Tahiyatul Asfihani, S.Si., M.Si}
\DeclareRobustCommand\Kaprodi[1]{%
   \renewcommand\@kaprodi{#1}
}

\newcommand\@NIPkaprodi{19870728 201404 2 001}
\DeclareRobustCommand\NIPKaprodi[1]{%
   \renewcommand\@NIPkaprodi{#1}
}

\newcommand\@petugasruangbaca{Djoko Priatin}
\DeclareRobustCommand\PetugasRBM[1]{%
   \renewcommand\@petugasruangbaca{#1}
}

\newcommand\@NPPruangbaca{197201012002121003}
\DeclareRobustCommand\NPPrbm[1]{%
   \renewcommand\@NPPruangbaca{#1}
}

\newcommand\@petugasperpus{}
\DeclareRobustCommand\PetugasPerpustakaan[1]{%
   \renewcommand\@petugasperpus{#1}
}

\newcommand\@NIPpetugasperpus{}
\DeclareRobustCommand\NIPPetugasPerpustakaan[1]{%
   \renewcommand\@NIPpetugasperpus{#1}
}

% ======================================
%  Mesin pemotong nama → inisial
% ======================================

\def\short@name#1 #2\relax{%
    \def\first@name{#1}%
    \def\rest@name{#2}%
    \first@name\ \process@initials#2 \relax
}

\def\process@initials#1 #2\relax{%
    \ifx#1\relax
    \else
        \MakeUppercase{#1}.%
        \process@initials#2 \relax
    \fi
}

\newcommand{\FormBukuLembarPembimbing}{
\newgeometry{left=2.5cm, right=2.5cm, top=1.4cm, bottom=1.5cm}
\thispagestyle{empty}
\parindent0pt
{\fontfamily{ptm}\selectfont

\begin{center}
{\fontfamily{ptm}\fontsize{20pt}{22pt}\selectfont\textbf{TANDA TERIMA}}
\end{center}

\vspace{0.6cm}

Kami yang bertanda tangan di bawah ini masing-masing telah menerima sebuah buku\\
laporan Tugas Akhir Periode Wisuda \@periodewisuda\ tahun \@tahunwisuda\ dari :

\vspace{0.6cm}

\renewcommand{\arraystretch}{1.5}
\begin{tabular}{@{}p{1.8cm}p{0.4cm}p{11.5cm}@{}}
\textbf{NAMA} & : & \@nama \\
\textbf{NRP} & : & \@NRP \\
\textbf{Judul TA} & : & \@judul \\
\end{tabular}
\renewcommand{\arraystretch}{1}

\vfill

\begin{center}
\ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
{
\begin{tabular}{c}
\textbf{PEMBIMBING}\vspace{2.1cm}\\
\underline{\textbf{\@pbbsatu}}\\
NIP. \@NIPpbbsatu
\end{tabular}
}
{
\begin{tabular}{>{\centering\arraybackslash}p{0.42\textwidth}>{\centering\arraybackslash}p{0.42\textwidth}}
\textbf{PEMBIMBING 1}\vspace{2.1cm} & \textbf{PEMBIMBING 2}\vspace{2.1cm}\\
\underline{\textbf{\@pbbsatu}} & \underline{\textbf{\@pbbdua}}\\
NIP. \@NIPpbbsatu & NIP. \@NIPpbbdua
\end{tabular}
}
\end{center}

\vfill

\begin{center}
\textbf{RUANG BACA Departemen \@jur\space FSAD-ITS}\\[1.6cm]
\underline{\textbf{\@petugasruangbaca}}\\
NPP. \@NPPruangbaca
\end{center}

\vfill

\begin{center}
\textbf{PERPUSTAKAAN PUSAT ITS}\\[2cm]
\ifthenelse{\equal{\@petugasperpus}{}\OR\equal{\@petugasperpus}{ }}
{(........................................)}%
{\underline{\textbf{\@petugasperpus}}}\\
NIP. \ifthenelse{\equal{\@NIPpetugasperpus}{}\OR\equal{\@NIPpetugasperpus}{ }}{........................................}{\@NIPpetugasperpus}
\end{center}

\vfill

Catatan : Form ini diserahkan kembali ke Kepala Program Studi Sarjana Matematika
}
}

\newcommand{\FormBukuLembarKaprodi}{
\newgeometry{left=2.5cm, right=2.5cm, top=1.4cm, bottom=1.5cm}
\thispagestyle{empty}
\parindent0pt
{\fontfamily{ptm}\selectfont

\begin{center}
{\fontfamily{ptm}\fontsize{20pt}{22pt}\selectfont\textbf{TANDA TERIMA}}
\end{center}

\vspace{0.6cm}

Saya yang bertanda tangan di bawah ini telah menerima sebuah buku laporan Tugas\\
Akhir Periode Wisuda \@periodewisuda\ tahun \@tahunwisuda\ dari :

\vspace{0.6cm}

\renewcommand{\arraystretch}{1.5}
\begin{tabular}{@{}p{1.8cm}p{0.4cm}p{11.5cm}@{}}
\textbf{NAMA} & : & \@nama \\
\textbf{NRP} & : & \@NRP \\
\textbf{Judul TA} & : & \@judul \\
\end{tabular}
\renewcommand{\arraystretch}{1}

\vfill

\begin{center}
\textbf{Kepala Program Studi Sarjana \@jur\space FSAD-ITS}\\[2.5cm]
\underline{\textbf{\@kaprodi}}\\
NIP. \@NIPkaprodi
\end{center}

\vfill

Catatan : Form ini diserahkan kembali ke Kepala Program Studi Sarjana Matematika
}
}

\newcommand{\FormSempro}{
\newgeometry{left=2cm, right=2cm, top=2cm, bottom=2cm}
\thispagestyle{fancy}

\fancyfoot[C]{%
  \parbox{\textwidth}{%
  \renewcommand{\arraystretch}{1}
    \centering
    \begin{tabular}{|>{\centering\arraybackslash}m{0.8\linewidth}|>{\centering\arraybackslash}m{0.15\linewidth}|}
    \hline
      \bfseries Prodi Sarjana - Departemen \@jur 
      & Halaman: \\ 
      \MakeUppercase{\bfseries Fakultas \@fak, ITS }
      % & \thepage\ dari \pageref{LastPage} \\
      & \thepage\ dari \thepage \\
    \hline
    \end{tabular}%
  }%
}

\noindent
\begin{table}[H]
    \centering
    \begin{tabular}{|m{3.5cm}|p{6cm}|p{3.5cm}|p{2.5cm}|}
    \hline
    % KOLOM 1: LOGO (Menggabungkan 3 baris ke bawah)
    \multirow{7}{*}{\centering\includegraphics[width=\linewidth]{logoITS.png}
    } 
    & 
    % BARIS 1 KOLOM 2: Header Departemen
    \multicolumn{3}{c|}{%
        \begin{tabular}[t]{c}
        \rule{0pt}{1.5em}
            \textbf{\Large \MakeUppercase{DEPARTEMEN \@jur}} \\
            \small {Kampus ITS Sukolilo, Surabaya 60111} \\
            \small {Telp/Fax: 031-5996506, Email: \href{mailto:matematika@its.ac.id}{\textcolor{linkblue}{\underline{matematika@its.ac.id}}}} \\
            \small \href{https://www.its.ac.id/matematika/}{\textcolor{linkblue}{\underline{https://www.its.ac.id/matematika/}}}
            \vspace{0.1cm}
        \end{tabular}%
    } \\
    \cline{2-4}
    
    % BARIS 2 KOLOM 2: Judul Form
    & \multicolumn{3}{c|}{%
    \begin{tabular}[t]{c}
        \vspace{0.1cm}
        \textbf{\large {FORM PENDAFTARAN SEMINAR PROPOSAL TA}}\\
        \textbf{\large {SEMESTER \@smt\ \@thnajr}}
        \vspace{0.1cm}
        \end{tabular}%
    } \\
    \cline{2-4}
    
    % BARIS 3: Footer Tabel (Nomor Dokumen, Edisi, Revisi)
    & \multicolumn{1}{l|}{Nomor Dokumen: Form TA-01} 
    & \multicolumn{1}{p{4cm}|}{Edisi: Juni 2024} 
    & \multicolumn{1}{p{2.5cm}|}{Revisi: \@rev} \\
    \hline
\end{tabular}
\end{table}

{\fontfamily{ptm}\selectfont
    Dengan ini kami menyatakan bahwa mahasiswa berikut ini telah layak untuk mengikuti seminar Proposal Tugas Akhir.
}
\renewcommand{\arraystretch}{2}
{
\begin{table}[H]
    \centering
    \carlitoTLF
    \begin{tabular}{|l p{13.5cm}|}
    \hline
         Nama   &:  \@nama\\
         NRP    &: \@NRP\\
         Laboratorium &: \@lab\\
         Judul Tugas Akhir &: \@judul\\[1em]
         \multicolumn{2}{|l|}{\textbf{Data Calon Dosen Pembimbing}}\\
        Nama   &:  \@pbbsatu\\
        NIP    &: \@NIPpbbsatu\\
        \hline
        \multicolumn{2}{|r|}{\begin{tabular}{l}
             Surabaya, \@tgl\ \@bulan\ \@tahun
        \end{tabular}}\\
        \multicolumn{2}{|c|}{%
    \ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
        {
\begin{tabular}{>{\centering\arraybackslash}p{0.4\linewidth}>{\centering\arraybackslash}p{0.4\linewidth}}
    \textbf{Mahasiswa} & \textbf{Dosen Pembimbing} \vspace{2cm}\\
    (\@nama) &(\underline{\@pbbsatu})                   \\
    NRP. \@NRP &NIP. \@NIPpbbsatu                       
\end{tabular}
        }
        {
          \begin{tabular}{>
          {\centering\arraybackslash}p{0.27\linewidth}>{\centering\arraybackslash}p{0.27\linewidth}>{\centering\arraybackslash}p{0.27\linewidth}}
\textbf{Mahasiswa}&\textbf{Dosen Pembimbing 1}\vspace{2cm}&\textbf{Dosen Pembimbing 2}\vspace{2cm}\\
 (\@nama)&   (\underline{\@pbbsatu}) & (\underline{\@pbbdua}) \\
  NRP. \@NRP &  NIP. \@NIPpbbsatu & NIP. \@NIPpbbdua
\end{tabular}}
        }\\
        \hline
    \end{tabular}
\end{table}
}
\renewcommand{\arraystretch}{1}

}

\newcommand{\FormCeklisSempro}{
\newgeometry{left=3cm, right=3cm, top=2.5cm, bottom=2.5cm}
\thispagestyle{empty}

\noindent
\begin{tabular}{m{2.2cm}m{12.8cm}}
\includegraphics[width=1.9cm]{logoITS.png} &
\begin{tabular}[c]{c}
\textbf{INSTITUT TEKNOLOGI SEPULUH NOPEMBER}\\
\textbf{\MakeUppercase{FAKULTAS \@fak}}\\
\textbf{\Large \MakeUppercase{DEPARTEMEN \@jur}}\\
\textbf{Program Studi Sarjana}
\end{tabular}
\end{tabular}

\vspace{0.2cm}
\hrule
\vspace{0.6cm}

\begin{center}
{\fontfamily{ptm}\fontsize{18pt}{20pt}\selectfont TANDA TERIMA}\\[0.3cm]
\textbf{BERKAS PENDAFTARAN SEMINAR PROPOSAL TUGAS AKHIR}\\[0.2cm]
\textbf{SEMESTER \MakeUppercase{\@smt} TAHUN \@thnajr}
\end{center}

\vspace{0.6cm}

\renewcommand{\arraystretch}{1.45}
\noindent
\begin{tabular}{|p{3.5cm} p{10.1cm}|}
\hline
Nama & :  \@nama \\
NRP & :  \@NRP \\
Calon Dosen Pembimbing & :  \DaftarPembimbing \\
Laboratorium/RMK & :  \@lab \\
Judul Tugas Akhir & :  \@judul \\
\hline
\end{tabular}

\vspace{0.7cm}

Beri tanda cek list ($\checkmark$) pada kotak yang disediakan

\vspace{0.3cm}

\renewcommand{\arraystretch}{1.2}
\begin{center}
\begin{tabular}{|c|p{10cm}|c|c|}
\hline
\textbf{No} & \textbf{Jenis Berkas} & \textbf{Ada} & \textbf{Tidak Ada} \\
\hline
1 & Bukti daftar di SIAMAT dan myITS Thesis & $\square$ & $\square$ \\
\hline
2 & Form Pendaftaran Seminar Proposal & $\square$ & $\square$ \\
\hline
3 & Draft Buku TA (4/5 eksemplar) & $\square$ & $\square$ \\
\hline
4 & Bukti Skor SKEM & $\square$ & $\square$ \\
\hline
5 & Bukti sudah menempuh minimal 110 SKS (transkrip sementara \& KRS terakhir) & $\square$ & $\square$ \\
\hline
6 & Bukti kelulusan TOEFL atau bukti keikutsertaan tes TOEFL terbaru (bagi yang belum lulus) & $\square$ & $\square$ \\
\hline
\end{tabular}
\end{center}

\vspace{0.5cm}

\noindent
\begin{tabular}{p{8.8cm}p{5.2cm}}
& Surabaya, \@tgl\ \@bulan\ \@tahun \\
& Penerima \\[2.3cm]
& (\textbf{\@pnrm}) \\
\end{tabular}

\renewcommand{\arraystretch}{1}
}

\newcommand{\FormCeklisUjianTA}{
\newgeometry{left=3cm, right=3cm, top=2.5cm, bottom=2.5cm}
\thispagestyle{empty}

\noindent
\begin{tabular}{m{2.2cm}m{12.8cm}}
\includegraphics[width=1.9cm]{logoITS.png} &
\begin{tabular}[c]{c}
\textbf{INSTITUT TEKNOLOGI SEPULUH NOPEMBER}\\
\textbf{\MakeUppercase{FAKULTAS \@fak}}\\
\textbf{\Large \MakeUppercase{DEPARTEMEN \@jur}}\\
\textbf{Program Studi Sarjana}
\end{tabular}
\end{tabular}

\vspace{0.2cm}
\hrule
\vspace{0.6cm}

\begin{center}
{\fontfamily{ptm}\fontsize{18pt}{20pt}\selectfont TANDA TERIMA}\\[0.3cm]
\textbf{BERKAS PENDAFTARAN UJIAN TUGAS AKHIR}\\[0.2cm]
\textbf{SEMESTER \MakeUppercase{\@smt} TAHUN \@thnajr}
\end{center}

\vspace{0.6cm}

\renewcommand{\arraystretch}{1.45}
\noindent
\begin{tabular}{|p{3.5cm} p{10.1cm}|}
\hline
Nama & :  \@nama \\
NRP & :  \@NRP \\
Dosen Pembimbing & :  \DaftarPembimbing \\
Laboratorium/RMK & :  \@lab \\
Judul Tugas Akhir & :  \@judul \\
\hline
\end{tabular}

\vspace{0.7cm}

Beri tanda cek list ($\checkmark$) pada kotak yang disediakan

\vspace{0.3cm}

\renewcommand{\arraystretch}{1.15}
\begin{center}
\begin{tabular}{|c|p{10cm}|c|c|}
\hline
\multirow{2}{*}{\textbf{No}} & \multirow{2}{*}{\textbf{Jenis Berkas}} & \multicolumn{2}{c|}{\textbf{Keterangan}} \\
\cline{3-4}
& & \textbf{Ada} & \textbf{Tidak Ada} \\
\hline
1 & Bukti daftar di SIAMAT dan myITS Thesis & $\square$ & $\square$ \\
\hline
2 & Form Pendaftaran Sidang (persetujuan dosen pembimbing) & $\square$ & $\square$ \\
\hline
3 & Draft Buku TA (5 buku) & $\square$ & $\square$ \\
\hline
4 & Makalah (5 eksemplar) & $\square$ & $\square$ \\
\hline
5 & Bukti telah melaksanakan bimbingan TA minimal 12 kali & $\square$ & $\square$ \\
\hline
6 & Sertifikat TOEFL & $\square$ & $\square$ \\
\hline
7 & Hasil Ithenticate (maks 25\%) & $\square$ & $\square$ \\
\hline
8 & Transkrip & $\square$ & $\square$ \\
\hline
\end{tabular}
\end{center}

\vspace{0.5cm}

\noindent
\begin{tabular}{p{8.8cm}p{5.2cm}}
& Surabaya, \@tgl\ \@bulan\ \@tahun \\
& Penerima \\[2.3cm]
& (\textbf{\@pnrm}) \\
\end{tabular}

\renewcommand{\arraystretch}{1}
}

\newcommand{\FormSemhas}{
\newgeometry{left=2cm, right=2cm, top=1.25cm, bottom=2cm}
\thispagestyle{fancy}

\fancyfoot[C]{%
  \parbox{\textwidth}{%
  \renewcommand{\arraystretch}{1}
    \centering
    \begin{tabular}{|>{\centering\arraybackslash}m{0.8\linewidth}|>{\centering\arraybackslash}m{0.15\linewidth}|}
    \hline
      \bfseries Prodi Sarjana - Departemen \@jur 
      & Halaman: \\ 
      \MakeUppercase{\bfseries Fakultas \@fak, ITS }
      % & \thepage\ dari \pageref{LastPage} \\
      % & \thepage\ dari \thepage \\
      & 1\ dari 1 \\
    \hline
    \end{tabular}%
  }%
}

\noindent
\begin{table}[H]
    \centering
    \begin{tabular}{|m{3.5cm}|p{6cm}|p{3.5cm}|p{2.5cm}|}
    \hline
    % KOLOM 1: LOGO (Menggabungkan 3 baris ke bawah)
    \multirow{7}{*}{\centering\includegraphics[width=\linewidth]{logoITS.png}
    } 
    & 
    % BARIS 1 KOLOM 2: Header Departemen
    \multicolumn{3}{c|}{%
        \begin{tabular}[t]{c}
        \rule{0pt}{1.5em}
            \textbf{\Large \MakeUppercase{DEPARTEMEN \@jur}} \\
            \small {Kampus ITS Sukolilo, Surabaya 60111} \\
            \small {Telp/Fax: 031-5996506, Email: \href{mailto:matematika@its.ac.id}{\textcolor{linkblue}{\underline{matematika@its.ac.id}}}} \\
            \small \href{https://www.its.ac.id/matematika/}{\textcolor{linkblue}{\underline{https://www.its.ac.id/matematika/}}}
            \vspace{0.1cm}
        \end{tabular}%
    } \\
    \cline{2-4}
    
    % BARIS 2 KOLOM 2: Judul Form
    & \multicolumn{3}{c|}{%
    \begin{tabular}[t]{c}
        \vspace{0.1cm}
        \textbf{\large {FORM PENDAFTARAN PAMERAN TUGAS AKHIR}}\\
        \textbf{\large {SEMESTER \@smt\ \@thnajr}}
        \vspace{0.1cm}
        \end{tabular}%
    } \\
    \cline{2-4}

    & \multicolumn{1}{l|}{Nomor Dokumen: Form TA-11} 
    & \multicolumn{1}{p{4cm}|}{Edisi: Januari 2026} 
    & \multicolumn{1}{p{2.5cm}|}{Revisi: \@rev} \\
    \hline
\end{tabular}
\end{table}

{\fontfamily{ptm}\selectfont
    Dengan ini kami menyatakan bahwa hasil Tugas Akhir mahasiswa berikut telah memenuhi kelayakan akademik untuk dipamerkan sesuai dengan ketentuan yang berlaku.
}
\renewcommand{\arraystretch}{2}
{
\begin{table}[H]
    \centering
    \carlitoTLF
    \begin{tabular}{|l p{13.5cm}|}
    \hline
         Nama   &:  \@nama\\
         NRP    &: \@NRP\\
         Laboratorium &: \@lab\\
         Judul Tugas Akhir &: \@judul\\[1em]
         \multicolumn{2}{|l|}{\textbf{Data Dosen Pembimbing}}\\
        Nama   &:  \@pbbsatu\\
        NIP    &: \@NIPpbbsatu\\
        \hline
        \multicolumn{2}{|r|}{\begin{tabular}{l}
             Surabaya, \@tgl\ \@bulan\ \@tahun
        \end{tabular}}\\
        \multicolumn{2}{|c|}{%
    \ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
        {
\begin{tabular}{>{\centering\arraybackslash}p{0.4\linewidth}>{\centering\arraybackslash}p{0.4\linewidth}}
    \textbf{Mahasiswa} & \textbf{Dosen Pembimbing} \vspace{2cm}\\
    (\@nama) &(\underline{\@pbbsatu})                   \\
    NRP. \@NRP &NIP. \@NIPpbbsatu                       
\end{tabular}
        }
        {
          \begin{tabular}{>
          {\centering\arraybackslash}p{0.27\linewidth}>{\centering\arraybackslash}p{0.27\linewidth}>{\centering\arraybackslash}p{0.27\linewidth}}
\textbf{Mahasiswa}&\textbf{Dosen Pembimbing 1}\vspace{2cm}&\textbf{Dosen Pembimbing 2}\vspace{2cm}\\
 (\@nama)&   (\underline{\@pbbsatu}) & (\underline{\@pbbdua}) \\
  NRP. \@NRP &  NIP. \@NIPpbbsatu & NIP. \@NIPpbbdua
\end{tabular}}
        }\\
        \hline
    \end{tabular}
\end{table}
}
\renewcommand{\arraystretch}{1}

}

\ExplSyntaxOn

\int_new:N \g_bimbingan_no_int
\tl_new:N \l_bimbingan_baris_tl

\cs_new_protected:Npn \bimbingan_buat_baris:n #1
{
  \int_gzero:N \g_bimbingan_no_int
  \tl_clear:N \l_bimbingan_baris_tl
  
  \seq_set_split:Nnn \l_tmpa_seq { \\ } {#1}
  \seq_map_inline:Nn \l_tmpa_seq
  {
    \tl_if_blank:nF {##1}
    {
      \int_gincr:N \g_bimbingan_no_int
      
      \tl_put_right:Nx \l_bimbingan_baris_tl { \int_use:N \g_bimbingan_no_int }
      \tl_put_right:Nn \l_bimbingan_baris_tl { & ##1 & \\ \hline }
    }
  }
  
  \tl_use:N \l_bimbingan_baris_tl
}

\NewDocumentCommand{\BuatBarisBimbingan}{m}
{
  \bimbingan_buat_baris:n {#1}
}

\ExplSyntaxOff

\NewDocumentEnvironment{BuktiBimbingan}{+b}
{%
\newgeometry{left=2cm, right=2cm, top=1.25cm, bottom=2cm}
\thispagestyle{fancy}

\fancyfoot[C]{%
  \parbox{\textwidth}{%
  \renewcommand{\arraystretch}{1}%
    \centering
    \begin{tabular}{|>{\centering\arraybackslash}m{0.8\linewidth}|>{\centering\arraybackslash}m{0.15\linewidth}|}
    \hline
      \bfseries Prodi Sarjana - Departemen \@jur
      & Halaman: \\
      \MakeUppercase{\bfseries Fakultas \@fak, ITS}
      & 1\ dari 1 \\
    \hline
    \end{tabular}%
  }%
}

\noindent
\begin{table}[H]
    \centering
    \begin{tabular}{|m{3.5cm}|p{6cm}|p{3.5cm}|p{2.5cm}|}
    \hline
    \multirow{7}{*}{\centering\includegraphics[width=\linewidth]{logoITS.png}}
    &
    \multicolumn{3}{c|}{%
        \begin{tabular}[t]{c}
        \rule{0pt}{1.5em}
            \textbf{\Large \MakeUppercase{DEPARTEMEN \@jur}} \\
            \small Kampus ITS Sukolilo, Surabaya 60111 \\
            \small Telp/Fax: 031-5996506, Email: \href{mailto:matematika@its.ac.id}{\textcolor{linkblue}{\underline{matematika@its.ac.id}}} \\
            \small \href{https://www.its.ac.id/matematika/}{\textcolor{linkblue}{\underline{https://www.its.ac.id/matematika/}}}
            \vspace{0.1cm}
        \end{tabular}%
    } \\
    \cline{2-4}

    &
    \multicolumn{3}{c|}{%
        \begin{tabular}[t]{c}
        \\
        \textbf{\Large Bukti Pembimbingan Tugas Akhir}
        \\
        \\
        \end{tabular}%
    } \\
    \cline{2-4}

    &
    \multicolumn{1}{l|}{Nomor Dokumen: Form TA-04}
    &
    \multicolumn{1}{p{4cm}|}{Edisi: Juni 2024}
    &
    \multicolumn{1}{p{2.5cm}|}{Revisi: \@rev} \\
    \hline
    \end{tabular}
\end{table}

\begin{table}[H]
    \centering
    \carlitoTLF
    \begin{tabular}{|l p{14cm}|}
    \hline
        Nama &: \@nama\\
        NRP &: \@NRP\\
        Judul &: \@judul\\
        Pembimbing &: \@pbbsatu\\
        &\\
        \multicolumn{2}{|c|}{%
            \begin{tabular}{|c|c|m{9.1cm}|m{3.5cm}|}
            \hline
            \rowcolor{cyan!20}
            \textbf{No}
            &
            \textbf{Tanggal}
            &
            \centering\textbf{Materi Bimbingan}
            &
            \centering\arraybackslash\textbf{Tanda Tangan/Paraf Pembimbing} \\
            \hline
            \rowcolor{cyan!0}
            \BuatBarisBimbingan{#1}
            \end{tabular}
        }\\&\\
        \hline
        \multicolumn{2}{|l|}{%
            \begin{tabular}{l}
            Surabaya, \@tgl\ \@bulan\ \@tahun
            \end{tabular}%
        }\\
        \multicolumn{2}{|c|}{%
        \ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
        {%
            \begin{tabular}{>{\centering\arraybackslash}p{0.4\linewidth}>{\centering\arraybackslash}p{0.4\linewidth}}
            \textbf{Dosen Pembimbing}\vspace{2cm} & \\
            (\underline{\@pbbsatu}) & \\
            NIP. \@NIPpbbsatu &
            \end{tabular}%
        }
        {%
            \begin{tabular}{>{\centering\arraybackslash}p{0.4\linewidth}>{\centering\arraybackslash}p{0.4\linewidth}}
            \textbf{Dosen Pembimbing 1}\vspace{2cm} & \textbf{Dosen Pembimbing 2}\vspace{2cm}\\
            (\underline{\@pbbsatu}) & (\underline{\@pbbdua}) \\
            NIP. \@NIPpbbsatu & NIP. \@NIPpbbdua
            \end{tabular}%
        }%
        }\\
        \hline
    \end{tabular}
\end{table}
}
{}

\newcommand{\FormSidang}{
\newgeometry{left=2cm, right=2cm, top=1.25cm, bottom=2cm}
\thispagestyle{fancy}

\fancyfoot[C]{%
  \parbox{\textwidth}{%
  \renewcommand{\arraystretch}{1}
    \centering
    \begin{tabular}{|>{\centering\arraybackslash}m{0.8\linewidth}|>{\centering\arraybackslash}m{0.15\linewidth}|}
    \hline
      \bfseries Prodi Sarjana - Departemen \@jur 
      & Halaman: \\ 
      \MakeUppercase{\bfseries Fakultas \@fak, ITS }
      % & \thepage\ dari \pageref{LastPage} \\
      % & \thepage\ dari \thepage \\
      & 1\ dari 1 \\
    \hline
    \end{tabular}%
  }%
}

\noindent
\begin{table}[H]
    \centering
    \begin{tabular}{|m{3.5cm}|p{6cm}|p{3.5cm}|p{2.5cm}|}
    \hline
    % KOLOM 1: LOGO (Menggabungkan 3 baris ke bawah)
    \multirow{7}{*}{\centering\includegraphics[width=\linewidth]{logoITS.png}
    } 
    & 
    % BARIS 1 KOLOM 2: Header Departemen
    \multicolumn{3}{c|}{%
        \begin{tabular}[t]{c}
        \rule{0pt}{1.5em}
            \textbf{\Large \MakeUppercase{DEPARTEMEN \@jur}} \\
            \small {Kampus ITS Sukolilo, Surabaya 60111} \\
            \small {Telp/Fax: 031-5996506, Email: \href{mailto:matematika@its.ac.id}{\textcolor{linkblue}{\underline{matematika@its.ac.id}}}} \\
            \small \href{https://www.its.ac.id/matematika/}{\textcolor{linkblue}{\underline{https://www.its.ac.id/matematika/}}}
            \vspace{0.1cm}
        \end{tabular}%
    } \\
    \cline{2-4}
    % BARIS 2 KOLOM 2: Judul Form
    & \multicolumn{3}{c|}{%
    \begin{tabular}[t]{c}
        \vspace{-0.4cm}\\
        \textbf{\large {FORM PENDAFTARAN PAMERAN TUGAS AKHIR}}\\
        \textbf{\large {SEMESTER \@smt\ \@thnajr}}
        \vspace{0.1cm}
        \end{tabular}%
    } \\
    \cline{2-4}

    & \multicolumn{1}{l|}{Nomor Dokumen: Form TA-03} 
    & \multicolumn{1}{p{4cm}|}{Edisi: Juni 2024} 
    & \multicolumn{1}{p{2.5cm}|}{Revisi: \@rev} \\
    \hline
\end{tabular}
\end{table}

{\fontfamily{ptm}\selectfont
    Dengan ini kami menyatakan bahwa mahasiswa berikut ini telah menyelesaikan Tugas Akhir dan layak untuk diujikan pada SIDANG Tugas Akhir.
}
\renewcommand{\arraystretch}{2}
{
\begin{table}[H]
    \centering
    \carlitoTLF
    \begin{tabular}{|l p{13.5cm}|}
    \hline
         Nama   &:  \@nama\\
         NRP    &: \@NRP\\
         Laboratorium &: \@lab\\
         Judul Tugas Akhir &: \@judul\\[1em]
         \multicolumn{2}{|l|}{\textbf{Data Dosen Pembimbing}}\\
        Nama   &:  \@pbbsatu\\
        NIP    &: \@NIPpbbsatu\\
        \hline
        \multicolumn{2}{|r|}{\begin{tabular}{l}
             Surabaya, \@tgl\ \@bulan\ \@tahun
        \end{tabular}}\\
        \multicolumn{2}{|c|}{%
    \ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
        {
\begin{tabular}{>{\centering\arraybackslash}p{0.4\linewidth}>{\centering\arraybackslash}p{0.4\linewidth}}
    \textbf{Mahasiswa} & \textbf{Dosen Pembimbing} \vspace{2cm}\\
    (\@nama) &(\underline{\@pbbsatu})                   \\
    NRP. \@NRP &NIP. \@NIPpbbsatu                       
\end{tabular}
        }
        {
          \begin{tabular}{>
          {\centering\arraybackslash}p{0.27\linewidth}>{\centering\arraybackslash}p{0.27\linewidth}>{\centering\arraybackslash}p{0.27\linewidth}}
\textbf{Mahasiswa}&\textbf{Dosen Pembimbing 1}\vspace{2cm}&\textbf{Dosen Pembimbing 2}\vspace{2cm}\\
 (\@nama)&   (\underline{\@pbbsatu}) & (\underline{\@pbbdua}) \\
  NRP. \@NRP &  NIP. \@NIPpbbsatu & NIP. \@NIPpbbdua
\end{tabular}}
        }\\
        \hline
    \end{tabular}
\end{table}
}
\renewcommand{\arraystretch}{1}

}
