%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%
%%% File `TA-ITS.cls' ini ditujukan untuk menulis laporan
%%% Tugas Akhir (Skripsi) menggunakan LaTeX untuk program sarjana
%%% di Institut Teknologi Sepuluh Nopember, Surabaya.
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
%%% Revisi oleh: Ridho Nur Rohman Wijaya
%%% Matematika ITS 2018
%%% <ridhonurrohmanwijaya@gmail.com>
%%% Revisi: Generalisasi dan penyempurnaan Format A4 (2022)
%%%
%%% Revisi oleh: Teosofi Hidayah Agung
%%% Matematika ITS 2022
%%% <teosofihidayahagung@gmail.com>
%%% Revisi: Pembaruan bibliografi menggunakan biblatex (2025)
%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%
\ProvidesClass{file/TA-ITS}[12/12/2010 v1.01]
\NeedsTeXFormat{LaTeX2e}
\LoadClass[a4paper,12pt,oneside,openright,final]{book}
\RequirePackage[hmargin={3cm,2cm},vmargin={3cm,2.5cm}]{geometry}
\RequirePackage{graphicx}
\RequirePackage{amssymb,amsmath,amsthm,amsfonts,indentfirst,
                tabularx,ifthen}
%\RequirePackage{nohyperref}
\RequirePackage{hyperref}
\hypersetup{ % Merubah warna link
    colorlinks,
    linkcolor={black},
    citecolor={black},
    urlcolor={black}
}
\RequirePackage{float}
\RequirePackage{setspace}
\RequirePackage{afterpage}
\RequirePackage{xcolor}
\RequirePackage{caption}
\RequirePackage{tikz}
\RequirePackage{etoolbox}
% \RequirePackage[nosectionbib]{apacite}
\RequirePackage{lmodern}
% \RequirePackage[authoryear]{natbib}
\RequirePackage[backend=biber,
    style=apa,
    maxcitenames=2,
    hyperref=true,        
    giveninits=true, 
    uniquename=init, 
    natbib,
    ]{biblatex}

\AtEveryBibitem{%
  \clearfield{volume}%
  \clearfield{number}%
  \clearfield{issue}%
  % \clearfield{journaltitle}%
  \clearfield{pages}%
}

\newrobustcmd*{\nextcitefullname}{%
  \AtNextCite{%
    \DeclareNameAlias{labelname}{given-family}%
    \togglefalse{abx@bool@giveninits}}}

\newcommand\citeauthorfullname{%
  \nextcitefullname\citeauthor}
  
\newcommand\Citeauthorfullname{%
  \nextcitefullname
  \Citeauthor}
  
\newcommand\textcitefullname{%
  \nextcitefullname
  \textcite}
  
\newcommand\Textcitefullname{%
  \nextcitefullname
  \textcite}

\DefineBibliographyStrings{english}{
  andothers = {dkk.,},
  and = {dan},
}

\RequirePackage{xpatch}

\xpatchbibmacro{cite}{%
      \printnames{labelname}%
    }{%
      \printtext[bibhyperref]{\printnames{labelname}}%
    }{}{}

\xpatchbibmacro{textcite}{%
      \printnames{labelname}%
    }{%
      \printtext[bibhyperref]{\printnames{labelname}}%
    }{}{}
  
  \xpatchbibmacro{parencite}{%
      \printnames{labelname}%
    }{%
      \printtext[bibhyperref]{\printnames{labelname}}%
    }{}{}
  
\xpatchbibmacro{citeauthor}
  {\printnames{labelname}}
  {\printtext[bibhyperref]{\printnames{labelname}}}
  {}{}

    \xpatchbibdriver{apa}{%
      \printnames{labelname}%
    }{%
      \printtext[bibhyperref]{\printnames{labelname}}%
    }{}{}

    \xpatchcmd{\textcite}
  {\usebibmacro{textcite}}
  {\bibhyperref{\usebibmacro{textcite}}}
  {}{}


\RequirePackage[euler]{textgreek}

\newcolumntype{L}[1]{>{\raggedright\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
\newcolumntype{C}[1]{>{\centering\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}
\newcolumntype{R}[1]{>{\raggedleft\let\newline\\\arraybackslash\hspace{0pt}}m{#1}}

\newcommand{\@judul}{Judul T.A.}
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
\newcommand\@pbbdua{Nama Pembimbing Kedua}
\newcommand\@pbbtiga{Nama Pembimbing Ketiga}
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

\def\cleardoublepage{\clearpage%
	\if@twoside
	\ifodd\c@page\else
	\vspace*{\fill}
	\hfill
	\begin{center}
		\emph{ }
	\end{center}
	\vspace{\fill}
	\thispagestyle{empty}
	\newpage
	\if@twocolumn\hbox{}\newpage\fi
	\fi
	\fi
}

\newcommand\Cover{%
    \cleardoublepage\thispagestyle{empty}
    \color{white}
    \begin{flushleft}
    \vspace*{-20mm}
    \hspace{-10mm}
    \includegraphics[height=2.5cm]{foto/logoITSBiru}\\
    \vspace{10mm}
    \changepagecolor{blue}\afterpage{\nopagecolor}
    \vspace{10mm}
    \setstretch{1.5}\noindent
    \textsf{
    {\fontsize{14}{2}\selectfont{\textbf{TUGAS AKHIR~ - ~SM234801}}}\\
    \vspace{2cm}
    {\fontsize{18}{2}\selectfont{\textbf{\MakeUppercase{\@judul}}}}\\
    \vspace{3cm}
    {\fontsize{14}{2}\selectfont{\textbf{\MakeUppercase{\@nama}}}
    }\\{\fontsize{14}{2}\selectfont{NRP \@NRP}}\\
    \vspace{2cm}
    {\fontsize{14}{2}\selectfont{Dosen Pembimbing}}\\
    \ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
        {{\fontsize{14}{2}\selectfont{\textbf{\@pbbsatu}}}\\
            NIP \@NIPpbbsatu\\\mbox{}\\}
        {{\fontsize{14}{2}\selectfont{\textbf{\@pbbsatu}}}\\
            NIP \@NIPpbbsatu\\
            {\fontsize{14}{2}\selectfont{\textbf{\@pbbdua}}}\\
            NIP \@NIPpbbdua\\
        }
    \vspace{1.0cm}
    \textbf{Program Studi Sarjana}\\
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
    \cleardoublepage\thispagestyle{empty}
    \begin{flushleft}
    \vspace*{-20mm}
    \hspace{-10mm}
    \includegraphics[height=2.5cm]{foto/logoITS}\\
    \vspace{10mm}
    {\color{blue}\makebox[\textwidth]{\rule{200cm}{10mm}}}\\ 
    \vspace{10mm}\setstretch{1.5}\noindent
    \textsf{
    {\fontsize{14}{2}\selectfont{\textbf{PROPOSAL TUGAS AKHIR~ - ~SM234801}}}\\
    \vspace{2cm}
    {\fontsize{18}{2}\selectfont{\textbf{\MakeUppercase{\@judul}}}}\\
    \vspace{2cm}
    {\fontsize{14}{2}\selectfont{\textbf{\MakeUppercase{\@nama}}}
    }\\{\fontsize{14}{2}\selectfont{NRP \@NRP}}\\
    \vspace{2cm}
    {\fontsize{14}{2}\selectfont{Dosen Pembimbing}}\\
    \ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
        {{\fontsize{14}{2}\selectfont{\textbf{\@pbbsatu}}}\\
            NIP \@NIPpbbsatu\\\mbox{}\\}
        {{\fontsize{14}{2}\selectfont{\textbf{\@pbbsatu}}}\\
            NIP \@NIPpbbsatu\\
            {\fontsize{14}{2}\selectfont{\textbf{\@pbbdua}}}\\
            NIP \@NIPpbbdua\\
        }
    \vspace{1.0cm}
    \textbf{Program Sarjana}\\
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
    \cleardoublepage\thispagestyle{empty}
    \begin{flushleft}
    \vspace*{-20mm}
    \hspace{-10mm}
    \includegraphics[height=2.5cm]{foto/logoITS}\\
    \vspace{10mm}
    {\color{blue}\makebox[\textwidth]{\rule{200cm}{10mm}}}\\
    \vspace{10mm}\setstretch{1.5}\noindent
    \textsf{
    {\fontsize{14}{2}\selectfont{\textbf{FINAL PROJECT PROPOSAL~ - ~SM234801}}}\\
    \vspace{2cm}
    {\fontsize{18}{2}\selectfont{\textbf{\MakeUppercase{\@juduleng}}}}\\
    \vspace{2cm}
    {\fontsize{14}{2}\selectfont{\textbf{\MakeUppercase{\@nama}}}
    }\\{\fontsize{14}{2}\selectfont{NRP \@NRP}}\\
    \vspace{1.5cm}
    {\fontsize{14}{2}\selectfont{Supervisor}}\\
    \ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
        {{\fontsize{14}{2}\selectfont{\textbf{\@pbbsatu}}}\\
            NIP \@NIPpbbsatu\\\mbox{}\\}
        {{\fontsize{14}{2}\selectfont{\textbf{\@pbbsatu}}}\\
            NIP \@NIPpbbsatu\\
            {\fontsize{14}{2}\selectfont{\textbf{\@pbbdua}}}\\
            NIP \@NIPpbbdua\\
        }
    \vspace{0.6cm}
    \textbf{Bachelor Program}\\
    Department of~\@dept\\
    Faculty of~\@fac\\
    Institut Teknologi Sepuluh Nopember\\
    Surabaya\\
    \@thn
    }
    \end{flushleft}
}

\newcommand\LembarPengesahan{%
\cleardoublepage
\setcounter{page}{1}
    \pagestyle{fancy}
    \fancyhf{}
    \fancyfoot[R]{\thepage}
    \setstretch{1}
\begin{center}
{\fontsize{14}{2}\selectfont{\textbf{LEMBAR PENGESAHAN}}}\vspace{1cm}\\
\textbf{\@judul}\vspace{0.75cm}\\
\textbf{PROPOSAL TUGAS AKHIR}\vspace{0.25cm}\\
Diajukan untuk memenuhi salah satu syarat\\memperoleh gelar Sarjana Matematika pada\\ Program Studi S-1 Matematika\\Departemen \@jur\\Fakultas \@fak\\Institut Teknologi Sepuluh Nopember\vspace{0.5cm}\\
        Oleh: \textbf{\@nama}\\
        NRP.~\@NRP\vspace{0.5cm}\\
       	Surabaya, \@bulan~\@thn\\
       	Disetujui oleh Tim Penguji Proposal Tugas Akhir:\\
       \vspace{0.5cm}
      \ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
        {
\begin{tabular}{ll}
\multicolumn{2}{c}{Pembimbing}\vspace{0.5cm}\\
1. \@pbbsatu & \hspace{1cm}(\dots\dots\dots\dots\dots\dots) \\
\hspace{0.5cm}NIP. \@NIPpbbsatu & \vspace{0.5cm}\\
\multicolumn{2}{c}{Penguji}\vspace{0.5cm}\\
1. \@pujsatu & \hspace{1cm}(\dots\dots\dots\dots\dots\dots) \\
\hspace{0.5cm}NIP. \@NIPpujsatu & \vspace{0.75cm}\\
2. \@pujdua & \hspace{1cm}(\dots\dots\dots\dots\dots\dots) \\
\hspace{0.5cm}NIP. \@NIPpujdua & \vspace{0.75cm}\\
3. \@pujtiga & \hspace{1cm}(\dots\dots\dots\dots\dots\dots) \\
\hspace{0.5cm}NIP. \@NIPpujtiga & \vspace{0.3cm}\\
\end{tabular}
        }
        {
\begin{tabular}{ll}
\multicolumn{2}{c}{Pembimbing}\vspace{0.5cm}\\
1. \@pbbsatu & \hspace{1cm}(\dots\dots\dots\dots\dots\dots) \\
\hspace{0.5cm}NIP. \@NIPpbbsatu & \vspace{0.5cm}\\
2. \@pbbdua & \hspace{1cm}(\dots\dots\dots\dots\dots\dots) \\
\hspace{0.5cm}NIP. \@NIPpbbdua & \vspace{0.1cm}\\
\multicolumn{2}{c}{Penguji}\vspace{0.5cm}\\
1. \@pujsatu & \hspace{1cm}(\dots\dots\dots\dots\dots\dots) \\
\hspace{0.5cm}NIP. \@NIPpujsatu & \vspace{0.5cm}\\
2. \@pujdua & \hspace{1cm}(\dots\dots\dots\dots\dots\dots) \\
\hspace{0.5cm}NIP. \@NIPpujdua & \vspace{0.5cm}\\
3. \@pujtiga & \hspace{1cm}(\dots\dots\dots\dots\dots\dots) \\
\hspace{0.5cm}NIP. \@NIPpujtiga & \vspace{0.2cm}\\
\end{tabular}
        }\\
    \begin{flushright}
    \begin{tabular}{c}
    Mengetahui                        \\
    Kepala Departemen Matematika      \\
    Fakultas Sains dan Analitika Data \vspace{2cm}\\
    \underline{\@kadep}                   \\
    NIP. \@NIPkadep                       
    \end{tabular}
    \end{flushright}
\end{center}
\addcontentsline{toc}{chapter}{LEMBAR PENGESAHAN}
}

%% Lembar Pengesahan Proposal
\newcommand\LembarPengesahanProposal{%
\cleardoublepage
\setcounter{page}{1}
    \pagestyle{fancy}
    \fancyhf{}
    \fancyfoot[R]{\thepage}
    \setstretch{1}
\begin{center}
{\fontsize{14}{2}\selectfont{\textbf{LEMBAR PENGESAHAN}}}\vspace{1cm}\\
\textbf{\@judul}\vspace{0.75cm}\\
\textbf{\textit{\@juduleng}}\vspace{0.75cm}\\
\textbf{PROPOSAL TUGAS AKHIR}\vspace{0.25cm}\\
Diajukan untuk memenuhi salah satu syarat\\memperoleh gelar Sarjana Matematika pada\\ Program Studi S-1 Matematika\\Departemen \@jur\\Fakultas \@fak\\Institut Teknologi Sepuluh Nopember\vspace{0.5cm}\\
        Oleh: \textbf{\@nama}\\
        NRP.~\@NRP\vspace{0.5cm}\\
       \vspace{0.3cm}
      \ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
        {
\begin{tabular}{c}
    Menyetujui,                        \\
    Dosen Pembimbing         \vspace{2.5cm}\\
    \underline{\@pbbsatu}                   \\
    NIP. \@NIPpbbsatu                       
\end{tabular}
        }
        {
          \begin{tabular}{>{\centering\arraybackslash}p{0.5\textwidth}>{\centering\arraybackslash}p{0.5\textwidth}}
Menyetujui,&Menyetujui,\\
Dosen Pembimbing 1\vspace{2.5cm}&Dosen Pembimbing 2\vspace{2cm}\\
    \underline{\@pbbsatu} & \underline{\@pbbdua} \\
    NIP. \@NIPpbbsatu & NIP. \@NIPpbbdua
\end{tabular}
        }\\
    \begin{center}
    \begin{tabular}{c}
    Mengetahui,                        \\
    Kepala Departemen Matematika FSAD-ITS  \vspace{2.5cm}\\
    \underline{\@kadep}                   \\
    NIP. \@NIPkadep                     
    \end{tabular} \vspace{1cm}\\
    Surabaya, \\ \@bulan~\@thn\\
    \end{center}
\end{center}
\addcontentsline{toc}{chapter}{LEMBAR PENGESAHAN}
}

\newcommand\LembarOrisinalitas{
\cleardoublepage
    \begin{center}
        {\fontsize{14}{2}\selectfont{\textbf{PERNYATAAN ORISINALITAS}}}
    \end{center}\vspace{1.5cm}
    \noindent
    Yang bertanda tangan disini:\vspace{1cm}\\
    \begin{tabular}{lcl}
        Nama Mahasiswa / NRP &:& \@namaa~/ \@NRP\vspace{0.15cm}\\
        Departemen &:& \@jur\vspace{0.15cm}\\
        \ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
              {Dosen Pembimbing / NIP &:& \@pbbsatu~/ \@NIPpbbsatu\\}
              {Dosen Pembimbing / NIP &:& 1.~ \@pbbsatu~/ \@NIPpbbsatu\\&& 2.~ \@pbbdua~/ \@NIPpbbdua\\}
    \end{tabular}\vspace{1cm}\\
 dengan ini menyatakan bahwa Tugas Akhir dengan judul “\@judul” adalah hasil karya sendiri, bersifat orisinal, dan ditulis dengan mengikuti kaidah penulisan ilmiah.\\\\
Bilamana di kemudian hari ditemukan ketidaksesuaian dengan pernyataan ini, maka saya bersedia menerima sanksi sesuai dengan ketentuan yang berlaku di Institut Teknologi Sepuluh Nopember.\\ \vspace{1cm}
    \ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
      {\begin{flushleft}
        \begin{tabular}{L{9cm}L{7cm}}
    		&Surabaya, \@tglsetuju\\
    		&\\
    		Mengetahui&\\
    		Dosen Pembimbing &Mahasiswa\\
    		&\\
    		&\\
    		&\\
    		&\\
    		&\\
    		\underline{\@pbbsatu}&\underline{\@namaa}\\
    		NIP. \@NIPpbbsatu &NRP. \@NRP
    	\end{tabular}
        \end{flushleft}}
      {\vspace{-0.5cm}\begin{flushleft}
        \begin{tabular}{L{9cm}L{7cm}}
    		&Surabaya, \@tglsetuju\\
    		&\\
    		Mengetahui&\\
    		Dosen Pembimbing 2&Dosen Pembimbing 1\\
    		&\\
    		&\\
    		&\\
    		&\\
    		\underline{\@pbbdua}&\underline{\@pbbsatu}\\
    		NIP. \@NIPpbbdua &NIP. \@NIPpbbsatu
    	\end{tabular}
        \end{flushleft}
        \begin{center}
            \begin{tabular}{c}
            \hspace{1cm}\\
            Mahasiswa\\
    		\hspace{1cm}\\
    		\hspace{1cm}\\
    		\hspace{1cm}\\
    		\hspace{1cm}\\
    		\underline{\@namaa}\\
    		NRP. \@NRP
    	    \end{tabular}
        \end{center}
      }
	\vspace{2cm}
\addcontentsline{toc}{chapter}{PERNYATAAN ORISINALITAS}
}

\newcommand\LembarAbstrak[1]{
\cleardoublepage
\setcounter{page}{2}
    \pagestyle{fancy}
    \fancyhf{}
    \fancyfoot[R]{\thepage}
    \setstretch{1}
  \begin{center}
        {\fontsize{14}{2}\selectfont{\textbf{ABSTRAK}}}\vspace{1.5cm}\\
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
          {Dosen Pembimbing &:& 1.~\@pbbsatu\\&& 2.~\@pbbdua\\&& 3.~\@pbbtiga}
    \end{tabular}\vspace{1cm}\\
  \addcontentsline{toc}{chapter}{ABSTRAK}
  \textbf{Abstrak}
  
  \input{#1}
  \setstretch{1}
  \par}{\normalfont\normalsize
  }

\newcommand\LembarAbstract{
\cleardoublepage
\begin{center}
        {\fontsize{14}{2}\selectfont{\textbf{ABSTRACT}}}\vspace{1.5cm}\\
        \@juduleng
    \end{center}\vspace{1cm}
  \begin{tabular}{lcl}
        Student Name / NRP &:& \@namaa~/ \@NRP\vspace{0.15cm}\\
        Departement &:& \@dept~\@singfakeng~- ITS\vspace{0.15cm}\\
        \ifthenelse{\equal{\@pbbtiga}{}\OR\equal{\@pbbtiga}{ }}
          {\ifthenelse{\equal{\@pbbdua}{}\OR\equal{\@pbbdua}{ }}
              {Supervisor &:& \@pbbsatu\\}
              {Advisor &:& 1.~ \@pbbsatu\\&& 2.~ \@pbbdua\\}
          }
          {Advisor &:& 1.~\@pbbsatu\\&& 2.~\@pbbdua\\&& 3.~\@pbbtiga}
    \end{tabular}\vspace{1cm}\\
  \addcontentsline{toc}{chapter}{ABSTRACT}
  \textbf{Abstract}
  
  \input{Inti/abstrakeng}
  \setstretch{1}
  \par}{\normalfont\normalsize
}


\newenvironment*{Abstrak}{%-------------------------------
  \cleardoublepage
  \begin{center}
        {\fontsize{14}{2}\selectfont{\textbf{ABSTRAK}}}\vspace{1.5cm}\\
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
  \par}{\normalfont\normalsize}
  
\newenvironment*{Abstract}{%-------------------------------
  \cleardoublepage
  \begin{center}
        {\fontsize{14}{2}\selectfont{\textbf{ABSTRACT}}}\vspace{1.5cm}\\
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
    \cleardoublepage
    \centerline{\large\bfseries KATA PENGANTAR}
    \addcontentsline{toc}{chapter}{KATA PENGANTAR}\vspace{1.5cm}
}
\newcommand{\UcapanTerimaKasih}{%-----------------
	\cleardoublepage
	\centerline{\large\bfseries UCAPAN TERIMA KASIH}
	\addcontentsline{toc}{chapter}{UCAPAN TERIMA KASIH}\vspace{1.5cm}
}
\newcommand{\DaftarIsi}{%---------------------
    \cleardoublepage
    \pagestyle{fancy}
    %\renewcommand\harvardand{dan}
    \addcontentsline{toc}{chapter}{DAFTAR ISI}
    \tableofcontents
}
\newcommand{\DaftarGambar}{%
    \ifnum\value{figure}>0
        \cleardoublepage
        \addcontentsline{toc}{chapter}{DAFTAR GAMBAR}%
        \listoffigures
    \fi
}

\newcommand{\DaftarTabel}{%
    \ifnum\value{table}>0
        \cleardoublepage
        \addcontentsline{toc}{chapter}{DAFTAR TABEL}%
        \listoftables
    \fi
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
   \cleardoublepage
   \addcontentsline{toc}{chapter}{LAMPIRAN}
   \begin{center}
    {\fontsize{14}{2}\selectfont{\textbf{LAMPIRAN}}}
    \end{center}

    \renewcommand\thesection{Lampiran \arabic{section}}
    \setcounter{chapter}{0}
    \setcounter{section}{0}
    \input{Inti/lampiran}
}
\newcommand{\DaftarSimbol}{%----------------------
    \cleardoublepage
    \addcontentsline{toc}{chapter}{DAFTAR SIMBOL}
    \begin{center}
    {\fontsize{14}{2}\selectfont{\textbf{DAFTAR SIMBOL}}}\vspace{1cm}
    \end{center}
    \input{Inti/daftar simbol}
}

%%%%---------------------------------
% \newcommand{\DaftarPustaka}{%---------------------
%     \cleardoublepage
%     % \addcontentsline{toc}{chapter}{DAFTAR PUSTAKA}
%     \renewcommand\bibname{DAFTAR PUSTAKA}
%     \bibliographystyle{apacite}
%     \bibliography{file/daftarPustaka}
%     }
\addbibresource{file/daftarPustaka.bib}
    \newcommand{\DaftarPustaka}{%
    \cleardoublepage
    \printbibliography[title={DAFTAR PUSTAKA}]
}

%%%%---------------------------------
\newcommand\BagianInti{%--------------------
    \cleardoublepage
    \mainmatter
    \pagestyle{fancy}
    \fancyfoot[R]{\thepage}
    \setstretch{1}
    % \fancyfoot[R]{\ifthenelse{\isodd{\value{page}}}{\thepage}{}}
    % \fancyfoot[L]{\ifthenelse{\isodd{\value{page}}}{}{\thepage}}

}
% \renewcommand\chapter{\if@openright\cleardoublepage\else\clearpage\fi
%                     \thispagestyle{fancy}%
%                     \global\@topnum\z@
%                     \@afterindentfalse
%                     \secdef\@chapter\@schapter}
\renewcommand\chapter{\cleardoublepage
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
    \vskip 40\p@
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
    \vskip 40\p@
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


%\newcommand\BukaLampiran{%
 % \cleardoublepage
 % \setcounter{chapter}{0}%
  %\setcounter{section}{0}%
 % \gdef\@chapapp{\appendixname}%
  %\gdef\thechapter{\@Alph\c@chapter}
  %\addtocontents{toc}{\protect\addvspace{1ex}}%
  %\addcontentsline{toc}{chapter}{LAMPIRAN}
  %\mbox{}\\\vfill
  %{\Huge \hfill{LAMPIRAN}}\\
  %\vfill\mbox{}\\
  %\thispagestyle{empty}
%}
%-----------------------------------
%\newcommand\lampiran[1]{%
   % \refstepcounter{chapter}
    %\cleardoublepage
    %\thispagestyle{fancy}
    %\addcontentsline{toc}{chapter}{\thechapter~~ #1}
    %\null
    %\begin{center}
    %\large\bfseries
    %\MakeUppercase\appendixname\space\thechapter
    %\par#1
    %\end{center}
    %\vskip 20\p@\par
%}
%-----------------------------------
\RequirePackage{file/picins}
\newcommand\Biodata[1]{%-----------
		\cleardoublepage
		\addcontentsline{toc}{chapter}{BIODATA PENULIS}
		\begin{center}
			{\fontsize{14}{2}\selectfont{\textbf{BIODATA PENULIS}}}\\\vspace{1cm}
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
% \renewcommand\bibname{DAFTAR PUSTAKA}
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

