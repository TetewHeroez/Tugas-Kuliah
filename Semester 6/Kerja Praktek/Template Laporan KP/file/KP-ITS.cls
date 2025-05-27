%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%
%%% File `KP-ITS.cls' ini ditujukan untuk menulis laporan
%%% Kerja praktek menggunakan LaTeX untuk Program Studi S-1
%%% di Institut Teknologi Sepuluh Nopember, Surabaya.
%%%
%%% File ini adalah hasil modifikasi dari `TA-ITS.cls'
%%%
%%% Komentar, saran, koreksi, modifikasi untuk file ini dipersilakan
%%%
%%% Dibuat oleh: Dr. Mahmud Yunus, M.Si
%%% NIP.19620407 198703 1 005
%%% <yunusm@matematika.its.ac.id>
%%%
%%% Revisi oleh: Mohamad Ilham Dwi Firmansyah
%%% Matematika ITS 2016
%%% <syah3946@gmail.com>
%%% Revisi: Format A5
%%%
%%% Revisi oleh: Alvian Alif Hidayatullah
%%% Matematika ITS 2018
%%% <alvinelbarca08@gmail.com>
%%% Revisi: Format A4 (2022)
%%%
%%% Revisi terahir oleh: Ridho Nur Rohman Wijaya
%%% Matematika ITS 2018
%%% <ridhonurrohmanwijaya@gmail.com>
%%% Revisi: Generalisasi dan penyempurnaan Format A4 (2022)
%%%
%%% Dimodifikasi untuk KP oleh: Teosofi Hidayah Agung
%%% Matematika ITS 2022
%%% <teosofihidayahagung@gmail.com>
%%% Modifikasi: Format dokumen KP (2025)
%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\ProvidesClass{file/KP-ITS}[21/05/2025 v1.00]
\NeedsTeXFormat{LaTeX2e}
\LoadClass[a5paper,11pt,oneside,openright,final]{book}
\RequirePackage[top=2.5cm,bottom=2.5cm,left=2.5cm,right=2.5cm]{geometry}
\RequirePackage{graphicx}
\RequirePackage{amssymb,amsmath,amsthm,amsfonts,indentfirst,tabularx,ifthen,arabtex}
%\RequirePackage{nohyperref}
\RequirePackage{hyperref}
\RequirePackage{float}
\RequirePackage{setspace}
\RequirePackage{afterpage}
\RequirePackage{times}
\RequirePackage[table]{xcolor}
\RequirePackage[nosectionbib]{apacite}

\newcolumntype{L}[1]{>{\raggedright\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
\newcolumntype{C}[1]{>{\centering\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
\newcolumntype{R}[1]{>{\raggedleft\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}

\newcommand{\@namaperusahaan}{Nama Perusahaan}
\DeclareRobustCommand{\NamaPerusahaan}[1]{%
    \renewcommand{\@namaperusahaan}{#1}%
}

\newcommand{\@judul}{Judul KP}
\DeclareRobustCommand{\Judul}[1]{%
    \renewcommand{\@judul}{#1}%
}
\newcommand{\@juduleng}{The Title}
\DeclareRobustCommand{\JudulEng}[1]{%
    \renewcommand{\@juduleng}{#1}%
}
\newcommand{\@nama}{Nama Mahasiswa}
\DeclareRobustCommand{\Nama}[1]{%
   \renewcommand{\@nama}{#1}%
}

\newcommand{\@namaa}{Nama Mahasiswa}
\DeclareRobustCommand{\NamaKecil}[1]{%
   \renewcommand{\@namaa}{#1}%
}

\newcommand{\@NRP}{1210100999}
\DeclareRobustCommand{\NRP}[1]{%
   \renewcommand{\@NRP}{#1}
}
\newcommand{\@alamat}{Jl. Himmel sang pahlawan No. 1}
\DeclareRobustCommand{\AlamatPenulis}[1]{%
   \renewcommand{\@alamat}{#1}
}
\newcommand\@jur{Matematika}
\DeclareRobustCommand\Departemen[1]{%
   \renewcommand\@jur{#1}
}
\newcommand\@dept{Mathematics}
\DeclareRobustCommand\Department[1]{%
   \renewcommand\@dept{#1}
}
\newcommand\@bidstudi{Pemodelan dan Simulasi Sistem}
\DeclareRobustCommand\BidangStudi[1]{%
   \renewcommand\@bidstudi{#1}
}
\newcommand\@thn{2010}
\DeclareRobustCommand\Tahun[1]{%
   \renewcommand\@thn{#1}
}

\newcommand\@bulan{Desember}
\DeclareRobustCommand\Bulan[1]{%
   \renewcommand\@bulan{#1}
}

\newcommand\@tglsetuju{12 Desember 2010}
\DeclareRobustCommand\TanggalDisetujui[1]{%
   \renewcommand\@tglsetuju{#1}
}

\newcommand\@fak{Matematika dan Ilmu Pengetahuan Alam}
\newcommand\@faks{MIPA}
\DeclareRobustCommand\Fakultas[2]{%
   \renewcommand\@fak{#1}
   \renewcommand\@faks{#2}
}
\newcommand\@fac{Mathematics and Natural Sciences}
\DeclareRobustCommand\Faculty[1]{%
   \renewcommand\@fac{#1}
}
\newcommand\@pbbsatu{Nama Pembimbing Pertama}
\newcommand\@pbbdua{Nama Pembimbing Ke-dua}
\newcommand\@pbbtiga{}
\DeclareRobustCommand\Pembimbing[3]{%
   \renewcommand{\@pbbsatu}{#1}%
   \renewcommand{\@pbbdua}{#2}%
   \renewcommand{\@pbbtiga}{#3}%
}
\newcommand\@NIPpbbsatu{12345678 123456 1 123}
\newcommand\@NIPpbbdua{12345678 123456 1 123}
\newcommand\@NIPpbbtiga{12345678 123456 1 123}
\DeclareRobustCommand\NIPPembimbing[3]{%
   \renewcommand{\@NIPpbbsatu}{#1}%
   \renewcommand{\@NIPpbbdua}{#2}%
   \renewcommand{\@NIPpbbtiga}{#3}%
}
\newcommand\@pujsatu{Nama Penguji Pertama}
\newcommand\@pujdua{Nama Penguji Ke-dua}
\newcommand\@pujtiga{}
\DeclareRobustCommand\Penguji[3]{%
   \renewcommand{\@pujsatu}{#1}%
   \renewcommand{\@pujdua}{#2}%
   \renewcommand{\@pujtiga}{#3}%
}
\newcommand\@NIPpujsatu{12345678 123456 1 123}
\newcommand\@NIPpujdua{12345678 123456 1 123}
\newcommand\@NIPpujtiga{12345678 123456 1 123}
\DeclareRobustCommand\NIPPenguji[3]{%
   \renewcommand{\@NIPpujsatu}{#1}%
   \renewcommand{\@NIPpujdua}{#2}%
   \renewcommand{\@NIPpujtiga}{#3}%
}

\newcommand\@NIPkadep{19710513 199702 1 001}
\DeclareRobustCommand\NIPKadep[1]{%
   \renewcommand\@NIPkadep{#1}
}

\newcommand\@kadep{Nama Kepala Departemen}
\DeclareRobustCommand\Kadep[1]{%
   \renewcommand\@kadep{#1}
}

\newcommand\@pbbmitra{Nama Pembimbing Mitra}
\DeclareRobustCommand\PembimbingMitra[1]{%
   \renewcommand\@pbbmitra{#1}
}

\newcommand\@NIPpbbmitra{19710513 199702 1 001}
\DeclareRobustCommand\NIPPembimbingMitra[1]{%
   \renewcommand\@NIPpbbmitra{#1}
}

\newcommand\@kaunit{Nama Kepala Perusahan/Unit}
\DeclareRobustCommand\KepalaInstansi[1]{%
   \renewcommand\@kaunit{#1}
}

\newcommand\@jbtkaunit{Jabatan Kepala Perusahan/Unit}
\DeclareRobustCommand\JabatanKepalaInstansi[1]{%
   \renewcommand\@jbtkaunit{#1}
}

\newcommand\@NIPkaunit{19710513 199702 1 001}
\DeclareRobustCommand\NIPKepalaInstansi[1]{%
   \renewcommand\@NIPkaunit{#1}
}

\newcommand\@singfak{FSAD}
\DeclareRobustCommand\SingkatanFakultas[1]{%
   \renewcommand\@singfak{#1}
}

\newcommand\@singfakeng{SCIENTICS}
\DeclareRobustCommand\SingkatanFakultasEng[1]{%
   \renewcommand\@singfakeng{#1}
}

\newcommand{\katakunci}[1]{%
    \vspace*{1ex}
    \noindent\\
    \begin{tabularx}{\textwidth}{@{}lX@{}}
        \textbf{Kata kunci:} & \textit{#1}
    \end{tabularx}
}
\newcommand{\keywords}[1]{%
    \vspace*{1ex}
    \noindent\\
    \begin{tabularx}{\textwidth}{@{}lX@{}}
        \textbf{Keywords:} & \textit{#1}
    \end{tabularx}
}

\newcommand\BagianAwal{%
    \frontmatter
    \newgeometry{bottom=1.2cm}
    % \pagestyle{fancy}
    % \fancyhf{}
    % \fancyfoot[R]{\thepage}
}
\definecolor{blue}{RGB}{0,103,172}
\renewcommand{\baselinestretch}{1}
\newcommand*{\changepagecolor}{%
  \@ifnextchar[\@changepagecolor@i\@changepagecolor@ii
}
% Case: \changepagecolor[...]{...}
\def\@changepagecolor@i[#1]#2{%
  \@changepagecolor@do{[{#1}]{#2}}%
}
% Case: \changepagecolor{...}
\newcommand*{\@changepagecolor@ii}[1]{%
  \@changepagecolor@do{{#1}}%
}
\newcommand*{\@changepagecolor@do}[1]{%
  % Fill the remaining space with a colored rule
  \begingroup
    \offinterlineskip
    \hbox to 0pt{%
      \kern-\paperwidth
      \vtop to 0pt{%
        \color#1%
        \hrule width 2\paperwidth height \paperheight
        \vss
      }%
      \hss
    }%
  \endgroup
  % Set page color for the next page
  \afterpage{\pagecolor#1}%
}
\newcommand\Cover{%
    \clearpage\thispagestyle{empty}
    \color{white}
    \begin{flushleft}
    \vspace*{-20mm}
    \hspace{-10mm}
    \includegraphics[height=2cm]{foto/logoITSBiru}\hfill\includegraphics[height=1cm]{foto/logoPerusahaan}\\
    \vspace{10mm}
    \changepagecolor{blue}\afterpage{\nopagecolor}
    \vspace{10mm}
    \setstretch{1.5}\noindent
    \textsf{
    {\fontsize{11}{2}\selectfont{\textbf{KERJA PRAKTIK~ - ~SM234701}}}\\
    \vspace{0.5cm}
    {\fontsize{12}{2}\selectfont{\textbf{\MakeUppercase{\@judul}}}}\\
    \vspace{1cm}
    {\fontsize{11}{2}\selectfont{\textbf{\MakeUppercase{\@nama}}}
    }\\{\fontsize{11}{2}\selectfont{NRP \@NRP}}\\
    \vspace{1cm}
    {\fontsize{11}{2}\selectfont{Dosen Pembimbing}}\\
    \ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
        {{\fontsize{11}{2}\selectfont{\textbf{\@pbbsatu}}}\\
            NIP \@NIPpbbsatu\\\mbox{}\\}
        {{\fontsize{11}{2}\selectfont{\textbf{\@pbbsatu}}}\\
            NIP \@NIPpbbsatu\\
            {\fontsize{11}{2}\selectfont{\textbf{\@pbbdua}}}\\
            NIP \@NIPpbbdua\\
        }
    \vspace{1cm}
    \textbf{Program Studi S-1}\\
    Departemen~\@jur\\
    Fakultas~\@fak\\
    Institut Teknologi Sepuluh Nopember\\
    Surabaya\\
    \@thn
    }
    \end{flushleft}
    \color{black}
    % \addcontentsline{toc}{chapter}{COVER}
}

\newcommand\LembarJudul{%
    \clearpage\thispagestyle{empty}
    \begin{flushleft}
    \vspace*{-20mm}
    \hspace{-10mm}
    \includegraphics[height=2cm]{foto/logoITS}\hfill\includegraphics[height=1cm]{foto/logoPerusahaan}\\
    \vspace{10mm}
    {\color{blue}\makebox[\textwidth]{\rule{200cm}{10mm}}}\\
    \vspace{5mm}\setstretch{1.5}\noindent
    \textsf{
    {\fontsize{11}{2}\selectfont{\textbf{KERJA PRAKTIK~ - ~SM234701}}}\\
    \vspace{0.5cm}
    {\fontsize{12}{2}\selectfont{\textbf{\MakeUppercase{\@judul}}}}\\
    \vspace{1cm}
    {\fontsize{11}{2}\selectfont{\textbf{\MakeUppercase{\@nama}}}
    }\\{\fontsize{11}{2}\selectfont{NRP \@NRP}}\\
    \vspace{1cm}
    {\fontsize{11}{2}\selectfont{Dosen Pembimbing}}\\
    \ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
        {{\fontsize{11}{2}\selectfont{\textbf{\@pbbsatu}}}\\
            NIP \@NIPpbbsatu\\\mbox{}\\}
        {{\fontsize{11}{2}\selectfont{\textbf{\@pbbsatu}}}\\
            NIP \@NIPpbbsatu\\
            {\fontsize{11}{2}\selectfont{\textbf{\@pbbdua}}}\\
            NIP \@NIPpbbdua\\
        }
    \vspace{1cm}
    \textbf{Program Studi S-1}\\
    Departemen~\@jur\\
    Fakultas~\@fak\\
    Institut Teknologi Sepuluh Nopember\\
    Surabaya\\
    \@thn
    }
    \end{flushleft}
    % \addcontentsline{toc}{chapter}{HALAMAN JUDUL}
}
\newcommand\TitlePage{%
    \clearpage\thispagestyle{empty}
    \begin{flushleft}
    \vspace*{-20mm}
    \hspace{-10mm}
    \includegraphics[height=2cm]{foto/logoITS}\hfill\includegraphics[height=1cm]{foto/logoPerusahaan}\\
    \vspace{10mm}
    {\color{blue}\makebox[\textwidth]{\rule{200cm}{10mm}}}\\
    \vspace{5mm}\setstretch{1.5}\noindent
    \textsf{
    {\fontsize{11}{2}\selectfont{\textbf{PRACTICAL WORK~ - ~SM234701}}}\\
    \vspace{0.5cm}
    {\fontsize{12}{2}\selectfont{\textbf{\MakeUppercase{\@juduleng}}}}\\
    \vspace{1cm}
    {\fontsize{11}{2}\selectfont{\textbf{\MakeUppercase{\@nama}}}
    }\\{\fontsize{11}{2}\selectfont{NRP \@NRP}}\\
    \vspace{1cm}
    {\fontsize{11}{2}\selectfont{Advisors}}\\
    \ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
        {{\fontsize{11}{2}\selectfont{\textbf{\@pbbsatu}}}\\
            NIP \@NIPpbbsatu\\\mbox{}\\}
        {{\fontsize{11}{2}\selectfont{\textbf{\@pbbsatu}}}\\
            NIP \@NIPpbbsatu\\
            {\fontsize{11}{2}\selectfont{\textbf{\@pbbdua}}}\\
            NIP \@NIPpbbdua\\
        }
    \vspace{1cm}
    \textbf{Study Program S-1}\\
    Departement of~\@dept\\
    Faculty of~\@fac\\
    Institut Teknologi Sepuluh Nopember\\
    Surabaya\\
    \@thn
    }
    \end{flushleft}
}

\newcommand\LembarPengesahanDepartemen{%
\clearpage
\newgeometry{bottom=2.5cm}
\setcounter{page}{1} 
\begin{center}
{\fontsize{12}{2}\selectfont{\textbf{LEMBAR PENGESAHAN DEPARTEMEN}}}\vspace{0.75cm}\\
\MakeUppercase{\textbf{laporan KERJA PRAKTIK \@namaperusahaan}}\vspace{0.5cm}\\
Diajukan untuk memenuhi salah satu syarat mata kuliah Kerja Praktik\\ Program Studi S-1 Matematika Departemen \@jur\\Fakultas \@fak\\Institut Teknologi Sepuluh Nopember\\Oleh\vspace{0.5cm}\\
\textbf{\@nama}\\
        \textbf{\@NRP}\vspace{0.5cm}\\
       	
Telah diperiksa dan disetujui sebagai Laporan Kerja Praktik pada\\
\underline{Surabaya, \@tglsetuju}\\
       \vspace{0.5cm}
\begin{tabular}{>{\centering\arraybackslash}p{0.5\textwidth}>{\centering\arraybackslash}p{0.5\textwidth}}
Mengetahui,&Menyetujui,\\
\shortstack{Kepala Departemen Matematika \\\@singfak-ITS}\vspace{2cm}&Dosen Pembimbing\vspace{2cm}\\\underline{\@kadep}&\underline{\@pbbsatu}\\
    NIP. \@NIPkadep & NIP. \@NIPpbbsatu
\vspace{0.5cm}
\end{tabular}
\end{center}
\addcontentsline{toc}{chapter}{LEMBAR PENGESAHAN DEPARTEMEN}
}

\newcommand\LembarPengesahanInstansi{%
\clearpage
\begin{center}
{\fontsize{12}{2}\selectfont{\textbf{LEMBAR PENGESAHAN INSTANSI}}}\vspace{0.75cm}\\
\MakeUppercase{\textbf{laporan KERJA PRAKTIK \@namaperusahaan}}\vspace{0.5cm}\\
Diajukan untuk memenuhi salah satu syarat mata kuliah Kerja Praktik\\ Program Studi S-1 Matematika Departemen \@jur\\Fakultas \@fak\\Institut Teknologi Sepuluh Nopember\\Oleh\vspace{0.5cm}\\
\textbf{\@nama}\\
        \textbf{\@NRP}\vspace{0.5cm}\\
       	
Telah diperiksa dan disetujui sebagai Laporan Kerja Praktik pada\\
\underline{Surabaya, \@tglsetuju}\\
       \vspace{0.5cm}
\begin{tabular}{>{\centering\arraybackslash}p{0.5\textwidth}>{\centering\arraybackslash}p{0.5\textwidth}}
Mengetahui,&Menyetujui,\\
\shortstack{\@jbtkaunit}\vspace{2cm}&Pembimbing Mitra\vspace{2cm}\\\underline{\@kaunit}&\underline{\@pbbmitra}\\
NIP. \@NIPkaunit & NIP. \@NIPpbbmitra
\vspace{0.5cm}
\end{tabular}
\end{center}
\addcontentsline{toc}{chapter}{LEMBAR PENGESAHAN INSTANSI}
}

\newcommand\LembarOrisinalitas{
\clearpage
    \begin{center}
        {\fontsize{12}{2}\selectfont{\textbf{PERNYATAAN ORISINALITAS}}}
    \end{center}
    \noindent
    Dengan ini, saya\\
    \renewcommand{\arraystretch}{1.2}
    \begin{tabular}{lcl}
        Nama&:& \@namaa\\
        NRP&:&\@NRP\\
        Departemen &:& \@jur\\
        Fakultas  &:& \@fak\\
        Alamat &:& \@alamat
    \end{tabular}\\~\\
 Menyatakan dengan sesungguhnya bahwa laporan kerja praktik dengan judul “\@judul”  hasil karya pribadi saya yang tidak mengandung plagiarisme, kecuali kutipan yang telah disebutkan sumbernya sesuai dengan ketentuan yang dibenarkan secara ilmuan.\\\\
Apabila pernyataan ini tidak benar, maka penulis siap bertanggung
jawab sesuai hukum yang berlaku dan ketentuan di Institut Teknologi Sepuluh Nopember.\\ \vspace{1cm}
\begin{flushright}
    \begin{tabular}{c}
    Surabaya, \@tglsetuju\\
    Penulis,\vspace{2cm}\\
    \textbf{\underline{\@nama}}\\
    \textbf{\@NRP}
    \end{tabular}
\end{flushright}
\addcontentsline{toc}{chapter}{PERNYATAAN ORISINALITAS}
}

\newenvironment*{Abstrak}{%-------------------------------
  \clearpage
  \begin{center}
        {\fontsize{12}{2}\selectfont{\textbf{ABSTRAK}}}\vspace{1.5cm}\\
        \@judul
    \end{center}\vspace{1cm}
  \begin{tabular}{lcl}
        Nama Mahasiswa / NRP &:& \@namaa~/ \@NRP\vspace{0.15cm}\\
        Departemen &:& \@jur~\@singfak~-ITS\vspace{0.15cm}\\
        \ifthenelse{\equal{\@pbbtiga}{}\OR\equal{\@pbbtiga}{ }}
          {\ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
              {Dosen Pembimbing &:& \@pbbsatu\\}
              {Dosen Pembimbing &:& 1.~ \@pbbsatu\\&& 2.~ \@pbbdua\\}
          }
          {\textbf{Dosen Pembimbing} &:& 1.~\@pbbsatu\\&& 2.~\@pbbsatu\\&& 3.~\@pbbsatu}
    \end{tabular}\vspace{1cm}\\
  \addcontentsline{toc}{chapter}{ABSTRAK}
  \textbf{Abstrak}
  \setstretch{1}
  \par}{\normalfont\normalsize
}
\newenvironment*{Abstract}{%-------------------------------
  \clearpage
  \begin{center}
        {\fontsize{12}{2}\selectfont{\textbf{ABSTRACT}}}\vspace{1.5cm}\\
        \@juduleng
    \end{center}\vspace{1cm}
  \begin{tabular}{lcl}
        Student Name / NRP &:& \@namaa~/ \@NRP\vspace{0.15cm}\\
        Departement &:& \@dept~\@singfakeng~- ITS\vspace{0.15cm}\\
        \ifthenelse{\equal{\@pbbtiga}{}\OR\equal{\@pbbtiga}{ }}
          {\ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
              {Advisor &:& \@pbbsatu\\}
              {Advisor &:& 1.~ \@pbbsatu\\&& 2.~ \@pbbdua\\}
          }
          {\textbf{Advisor} &:& 1.~\@pbbsatu\\&& 2.~\@pbbsatu\\&& 3.~\@pbbsatu}
    \end{tabular}\vspace{1cm}\\
  \addcontentsline{toc}{chapter}{ABSTRACT}
  \textbf{Abstract}
  \setstretch{1}
  \par}{\normalfont\normalsize
}
\newcommand{\KataPengantar}{%-----------------
    \clearpage
    \centerline{\large\bfseries KATA PENGANTAR}
    \addcontentsline{toc}{chapter}{KATA PENGANTAR}\vspace{1.5cm}
}
\newcommand{\UcapanTerimaKasih}{%-----------------
	\clearpage
	\centerline{\large\bfseries UCAPAN TERIMA KASIH}
	\addcontentsline{toc}{chapter}{UCAPAN TERIMA KASIH}\vspace{1.5cm}
}
\newcommand{\DaftarIsi}{%---------------------
    \clearpage
    \pagestyle{fancy}
    %\renewcommand\harvardand{dan}
    \addcontentsline{toc}{chapter}{DAFTAR ISI}
    \tableofcontents
}
\newcommand{\DaftarGambar}{%----------------------
    \clearpage
    \addcontentsline{toc}{chapter}{DAFTAR GAMBAR}
    \listoffigures
}
\newcommand{\DaftarTabel}{%----------------------
    \clearpage
    \addcontentsline{toc}{chapter}{DAFTAR TABEL}
    \listoftables
}

\newcommand\Lampiran[1]{%
    \refstepcounter{section}
    \addcontentsline{toc}{section}{\thesection~~ #1}
    \begin{center}
        \large\bfseries
        \thesection\\#1
    \end{center}
}
\newcommand{\DaftarLampiran}{%----------------------
   \clearpage
   \addcontentsline{toc}{chapter}{DAFTAR LAMPIRAN}
   \begin{center}
    {\fontsize{12}{2}\selectfont{\textbf{DAFTAR LAMPIRAN}}}
    \end{center}

    \renewcommand\thesection{Lampiran \arabic{section}}
    \setcounter{chapter}{0}
    \setcounter{section}{0}
}
\newcommand{\DaftarSimbol}{%----------------------
    \clearpage
    \addcontentsline{toc}{chapter}{DAFTAR SIMBOL}
    \begin{center}
    {\fontsize{12}{2}\selectfont{\textbf{DAFTAR SIMBOL}}}\vspace{0.1cm}
    \end{center}
}

%%%%---------------------------------
\newcommand{\DaftarPustaka}{%---------------------
    \clearpage
    % \addcontentsline{toc}{chapter}{DAFTAR PUSTAKA}
    \renewcommand\bibname{DAFTAR PUSTAKA}
    \fancyhead[R]{\footnotesize DAFTAR PUSTAKA}
    \bibliographystyle{apacite}
    \bibliography{file/daftarPustaka}
    }
%%%%---------------------------------
\newcommand\BagianInti{%--------------------
    \clearpage
    \mainmatter
    \pagestyle{fancy}
    \fancyhf{}
    \newgeometry{
      top=1.6cm,
      bottom=1.6cm,
      left=2.5cm,
      right=2cm,
      headsep=1cm,
      footskip=1cm
    }
    \fancyhead[L]{\includegraphics[width=2cm]{foto/logoITSBiru.png}\quad\includegraphics[width=1.8cm]{foto/LogoPerusahaan.png}}
    \renewcommand{\headrulewidth}{0.4pt}
    \fancyfoot[R]{\thepage}
    \setstretch{1}
}
\renewcommand\chapter{\clearpage
                    \thispagestyle{fancy}%
                    \global\@topnum\z@
                    \@afterindentfalse
                    \secdef\@chapter\@schapter}
\gdef\@chapter[#1]#2{\ifnum \c@secnumdepth >\m@ne
    \if@mainmatter
    \refstepcounter{chapter}%
    \typeout{\@chapapp\space\thechapter.}%
        \addcontentsline{toc}{chapter}%
        {\protect\numberline{\@chapapp\space\thechapter}#1}%
        \else
        \addcontentsline{toc}{chapter}{\@chapapp\space#1}%
            \fi
        \else
    \addcontentsline{toc}{chapter}{#1}%
                    \fi
                    \chaptermark{#1}%
                    \fancyhead[R]{\footnotesize BAB \thechapter\\#1}
                    \addtocontents{lof}{\protect\addvspace{10\p@}}%
                    \addtocontents{lot}{\protect\addvspace{10\p@}}%
                    \if@twocolumn
                      \@topnewpage[\@makechapterhead{#2}]%
                    \else
                      \@makechapterhead{#2}%
                      \@afterheading
                    \fi}
\gdef\@makechapterhead#1{%
  \vspace*{5\p@}%
  {\parindent \z@ \centering\normalfont
    \ifnum \c@secnumdepth >\m@ne
      \if@mainmatter
        \large\bfseries \MakeUppercase\@chapapp\space \thechapter
        \par
      \fi
    \fi
    \large\bfseries\MakeUppercase{#1}\par\nobreak
    \vskip 15\p@
  }}
\gdef\@schapter#1{\@makeschapterhead{#1}%
                 \@afterheading
                 }
\gdef\@makeschapterhead#1{%
  \vspace*{5\p@}%
  {\parindent \z@ \centering
    \normalfont
    \interlinepenalty\@M
    \large\bfseries\MakeUppercase{#1}\par\nobreak
    \vskip 15\p@
}}
\renewcommand\section{\@startsection {section}{1}{\z@}%
                                   {-1.5ex \@plus -1ex \@minus -.2ex}%
                                   {.01ex \@plus.2ex}%
                                   {\normalfont\normalsize\bfseries}}
\renewcommand\subsection{\@startsection{subsection}{2}{\z@}%
                                     {-1.5ex\@plus -1ex \@minus -.2ex}%
                                     {.01ex \@plus .2ex}%
                                     {\normalfont\normalsize\bfseries}}
\renewcommand\subsubsection{\@startsection{subsubsection}{3}{\z@}%
                                     {-.25ex\@plus -1ex \@minus -.2ex}%
                                     {.01ex \@plus.2ex}%
                                     {\normalfont\normalsize\bfseries}}
\renewcommand\paragraph{\@startsection{paragraph}{4}{\z@}%
                                    {.25ex \@plus1ex \@minus.2ex}%
                                    {-1.5em}%
                                    {\normalfont\normalsize\bfseries}}
\renewcommand*\thechapter{\@Roman\c@chapter}
\renewcommand*\thesection{\@arabic\c@chapter.\@arabic\c@section}

%%%-------------setting daftar isi/tabel/gambar------------------
\renewcommand\@dotsep{2}
\renewcommand*\l@chapter[2]{%
  \ifnum \c@tocdepth >\m@ne
    \addpenalty{-\@highpenalty}%
    \vskip 0.5em \@plus\p@
    \setlength\@tempdima{5em}%
    \begingroup
      \parindent \z@ \rightskip \@pnumwidth
      \parfillskip -\@pnumwidth
      \leavevmode %\bfseries
      \advance\leftskip\@tempdima
      \hskip -\leftskip
      #1\nobreak\hfil \nobreak
      \hb@xt@\@pnumwidth{\hss #2}
      \par
      \penalty\@highpenalty
    \endgroup
  \fi}
\renewcommand*\l@section{\@dottedtocline{1}{2.8em}{2.2em}}
\renewcommand*\l@subsection{\@dottedtocline{2}{5em}{2.75em}}
\renewcommand*\l@subsubsection{\@dottedtocline{3}{7.8em}{4.1em}}
\renewcommand*\l@figure{\@dottedtocline{1}{1.5em}{6em}}
\renewcommand*\l@table{\@dottedtocline{1}{1.5em}{5em}}
%%%%%%------------------------
\renewcommand\theequation
  {\ifnum \c@chapter>\z@ \@arabic\c@chapter.\fi \@arabic\c@equation}
\renewcommand \thefigure
     {\ifnum \c@chapter>\z@ \figurename\space \@arabic\c@chapter.\fi \@arabic\c@figure}
\def\fnum@figure{\nobreakspace\thefigure}
\renewcommand \thetable
     {\ifnum \c@chapter>\z@ \tablename\space  \@arabic\c@chapter.\fi \@arabic\c@table}
\def\fnum@table{\nobreakspace\thetable}

\def\@citex[#1]#2{%
  \let\@citea\@empty
  \@cite{\@for\@citeb:=#2\do
    {\@citea\def\@citea{,}%
     \edef\@citeb{\expandafter\@firstofone\@citeb\@empty}%
     \if@filesw\immediate\write\@auxout{\string\citation{\@citeb}}\fi
     \@ifundefined{b@\@citeb}{\mbox{\reset@font\bfseries ?}%
       \G@refundefinedtrue
       \@latex@warning
         {Citation `\@citeb' on page \thepage \space undefined}}%
       {\hbox{\csname b@\@citeb\endcsname}}}}{#1}}
%-----------------------------------
\newcommand\BukaLampiran{%
 \clearpage
 \setcounter{chapter}{0}%
  \setcounter{section}{0}%
 \gdef\@chapapp{\appendixname}%
  \gdef\thechapter{\@Alph\c@chapter}
  \addtocontents{toc}{\protect\addvspace{1ex}}%
  \addcontentsline{toc}{chapter}{LAMPIRAN}
  \mbox{}\\\vfill
  {\Huge \hfill{LAMPIRAN}}\\
  \vfill\mbox{}\\
  \thispagestyle{empty}
}
%-----------------------------------
\newif\if@appendixstarted
\@appendixstartedfalse
\newcommand\lampiran[1]{%
    \if@appendixstarted\else
   \appendix
   \setcounter{chapter}{0}
   \@appendixstartedtrue
\fi
   \refstepcounter{chapter}
    \clearpage
    % \setcounter{chapter}{1}
    % \gdef\thechapter{\@Alph\c@chapter}
    \thispagestyle{fancy}
    \addcontentsline{toc}{chapter}{Lampiran \thechapter. #1}
    \null
    \fancyhead[R]{\footnotesize LAMPIRAN}
    \begin{center}
    \large\bfseries
    \MakeUppercase\appendixname\space\thechapter
    \par#1
    \end{center}
    \vskip 15\p@\par
}

%-----------------------------------
\RequirePackage{file/picins}
\newcommand\Biodata[1]{%-----------
		\clearpage
		\addcontentsline{toc}{chapter}{BIODATA PENULIS}
        \fancyhead[R]{\footnotesize BIODATA PENULIS}
		\begin{center}
            $\,$\\
			{\fontsize{12}{2}\selectfont{\textbf{BIODATA PENULIS}}}\\
		\end{center}
\thispagestyle{fancy}
  \newsavebox{\foto}
  \savebox{\foto}[4cm][b]{\includegraphics[width=4cm,height=6cm]{#1}}
  \parpic(4cm,6cm){\usebox\foto}
}

%%%------------- PENYESUAIAN ISTILAH ---------------------------
\renewcommand\contentsname{DAFTAR ISI}
\renewcommand\listfigurename{DAFTAR GAMBAR}
\renewcommand\listtablename{DAFTAR TABEL}
\renewcommand\bibname{DAFTAR PUSTAKA}
\renewcommand\indexname{INDEKS}
\renewcommand\figurename{Gambar}
\renewcommand\tablename{Tabel}
\renewcommand\chaptername{BAB}
\renewcommand\appendixname{Lampiran}

\lefthyphenmin=10
\righthyphenmin=10
\sloppy

\newcommand{\kb}[1]{\left(#1\right)}
%%
%% end of file `TA-ITS.cls'.

