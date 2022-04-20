%global __provides_exclude %{?__provides_exclude:%__provides_exclude|}^perl\\(
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\((LatexIndent.*|PDF::Reuse.*|Pedigree.*|TeXLive.*|Tk::path_tre)\\)
%global __brp_mangle_shebangs_exclude ^$

Name:           texlive-base
Version:        20180414
Release:        34
Epoch:          7
Summary:        TeX formatting system
License:        ASL 2.0 and LGPL-2.1-only and Zlib and OFL-1.1 and Public Domain and LGPL-2.0-only and GPLv2+ and MPL-1.1 and Libpng and LGPL-3.0-only and BSL-1.0 and GPLv2 and GPLv3 and CPL-1.0 and IJG and MIT and LPPL-1.3c and ICU and psutils
URL:            http://tug.org/texlive/
Source0:	https://sourceforge.net/projects/mylfs/files/sources/texlive-20180414-source.tar.xz
Source1:        macros.texlive
Source2:        texlive.tlpdb
Source3:        texlive-licenses.tar.xz
Source4:        generate-fmtutilcnf
Source5:        http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cyrillic.tar.xz
Source6:        http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cyrillic.doc.tar.xz
Source7:        http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glyphlist.tar.xz
Source8:        http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex.tar.xz
Source9:        http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex.doc.tar.xz
Source10:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lyluatex.tar.xz
Source11:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lyluatex.doc.tar.xz
Source12:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oberdiek.tar.xz
Source13:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/oberdiek.doc.tar.xz
Source14:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-en.doc.tar.xz
Source15:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/a2ping.doc.tar.xz
Source16:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/a2ping.tar.xz
Source17:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/accfonts.doc.tar.xz
Source18:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/accfonts.tar.xz
Source19:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adhocfilelist.doc.tar.xz
Source20:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/adhocfilelist.tar.xz
Source21:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/afm2pl.tar.xz
Source22:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aleph.doc.tar.xz
Source23:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/aleph.tar.xz
Source24:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amstex.doc.tar.xz
Source25:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/amstex.tar.xz
Source26:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arara.doc.tar.xz
Source27:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/arara.tar.xz
Source28:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/authorindex.doc.tar.xz
Source29:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/authorindex.tar.xz
Source30:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/autosp.doc.tar.xz
Source31:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/axodraw2.doc.tar.xz
Source32:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/axodraw2.tar.xz
Source33:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bib2gls.doc.tar.xz
Source34:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bib2gls.tar.xz
Source35:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibexport.doc.tar.xz
Source36:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibexport.tar.xz
Source37:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibtex8.doc.tar.xz
Source38:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibtex8.tar.xz
Source39:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibtex.doc.tar.xz
Source40:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibtex.tar.xz
Source41:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bibtexu.doc.tar.xz
Source42:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bundledoc.doc.tar.xz
Source43:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bundledoc.tar.xz
Source44:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cachepic.doc.tar.xz
Source45:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cachepic.tar.xz
Source46:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/checkcites.doc.tar.xz
Source47:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/checkcites.tar.xz
Source48:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/checklistings.doc.tar.xz
Source49:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/checklistings.tar.xz
Source50:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chktex.doc.tar.xz
Source51:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chktex.tar.xz
Source52:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cjk-gs-integrate.doc.tar.xz
Source53:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cjk-gs-integrate.tar.xz
Source54:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cjkutils.tar.xz
Source55:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context.doc.tar.xz
Source56:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/context.tar.xz
Source57:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/convbkmk.doc.tar.xz
Source58:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/convbkmk.tar.xz
Source59:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crossrefware.doc.tar.xz
Source60:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/crossrefware.tar.xz
Source61:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cslatex.tar.xz
Source62:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/csplain.tar.xz
Source63:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctanify.doc.tar.xz
Source64:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctanify.tar.xz
Source65:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctan-o-mat.doc.tar.xz
Source66:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctan-o-mat.tar.xz
Source67:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctanupload.doc.tar.xz
Source68:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctanupload.tar.xz
Source69:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ctie.doc.tar.xz
Source70:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cweb.doc.tar.xz
Source71:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cweb.tar.xz
Source72:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cyrillic-bin.doc.tar.xz
Source73:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cyrillic-bin.tar.xz
Source74:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/de-macro.doc.tar.xz
Source75:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/de-macro.tar.xz
Source76:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/detex.doc.tar.xz
Source77:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/detex.tar.xz
Source78:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/diadia.doc.tar.xz
Source79:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/diadia.tar.xz
Source80:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dosepsbin.doc.tar.xz
Source81:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dosepsbin.tar.xz
Source82:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dtl.doc.tar.xz
Source83:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dtl.tar.xz
Source84:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dtxgen.doc.tar.xz
Source85:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dtxgen.tar.xz
Source86:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvi2tty.doc.tar.xz
Source87:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvi2tty.tar.xz
Source88:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dviasm.doc.tar.xz
Source89:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dviasm.tar.xz
Source90:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvicopy.doc.tar.xz
Source91:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvicopy.tar.xz
Source92:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvidvi.doc.tar.xz
Source93:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvidvi.tar.xz
Source94:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dviinfox.doc.tar.xz
Source95:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dviinfox.tar.xz
Source96:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dviljk.doc.tar.xz
Source97:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dviljk.tar.xz
Source98:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvipdfmx.doc.tar.xz
Source99:       http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvipdfmx.tar.xz
Source100:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvipng.doc.tar.xz
Source101:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvipng.tar.xz
Source102:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvipos.doc.tar.xz
Source103:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvipos.tar.xz
Source104:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvips.doc.tar.xz
Source105:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvips.tar.xz
Source106:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvisvgm.doc.tar.xz
Source107:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/dvisvgm.tar.xz
Source108:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ebong.doc.tar.xz
Source109:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ebong.tar.xz
Source110:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eplain.doc.tar.xz
Source111:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/eplain.tar.xz
Source112:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epspdf.doc.tar.xz
Source113:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epspdf.tar.xz
Source114:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epstopdf.doc.tar.xz
Source115:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/epstopdf.tar.xz
Source116:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exceltex.doc.tar.xz
Source117:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/exceltex.tar.xz
Source118:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fig4latex.doc.tar.xz
Source119:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fig4latex.tar.xz
Source120:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/findhyph.doc.tar.xz
Source121:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/findhyph.tar.xz
Source122:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontinst.doc.tar.xz
Source123:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontinst.tar.xz
Source124:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontools.doc.tar.xz
Source125:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontools.tar.xz
Source126:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fontware.doc.tar.xz
Source127:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fragmaster.doc.tar.xz
Source128:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/fragmaster.tar.xz
Source129:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/getmap.doc.tar.xz
Source130:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/getmap.tar.xz
Source131:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries.doc.tar.xz
Source132:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/glossaries.tar.xz
Source133:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gregoriotex.doc.tar.xz
Source134:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gregoriotex.tar.xz
Source135:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gsftopk.doc.tar.xz
Source136:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/gsftopk.tar.xz
Source137:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/installfont.doc.tar.xz
Source138:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/installfont.tar.xz
Source139:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jadetex.doc.tar.xz
Source140:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jadetex.tar.xz
Source141:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jfmutil.doc.tar.xz
Source142:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/jfmutil.tar.xz
Source143:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kotex-utils.doc.tar.xz
Source144:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kotex-utils.tar.xz
Source145:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kpathsea.doc.tar.xz
Source146:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/kpathsea.tar.xz
Source147:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/l3build.tar.xz
Source148:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/l3build.doc.tar.xz
Source149:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lacheck.doc.tar.xz
Source150:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex2man.doc.tar.xz
Source151:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex2man.tar.xz
Source152:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex2nemeth.doc.tar.xz
Source153:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex2nemeth.tar.xz
Source154:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexdiff.doc.tar.xz
Source155:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexdiff.tar.xz
Source156:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexfileversion.doc.tar.xz
Source157:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexfileversion.tar.xz
Source158:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-git-log.doc.tar.xz
Source159:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-git-log.tar.xz
Source160:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexindent.doc.tar.xz
Source161:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexindent.tar.xz
Source162:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexpand.doc.tar.xz
Source163:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latexpand.tar.xz
Source164:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-papersize.doc.tar.xz
Source165:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/latex-papersize.tar.xz
Source166:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lcdftypetools.doc.tar.xz
Source167:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lilyglyphs.doc.tar.xz
Source168:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lilyglyphs.tar.xz
Source169:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listbib.doc.tar.xz
Source170:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listbib.tar.xz
Source171:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listings-ext.doc.tar.xz
Source172:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/listings-ext.tar.xz
Source173:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lollipop.doc.tar.xz
Source174:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lollipop.tar.xz
Source175:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltxfileinfo.doc.tar.xz
Source176:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltxfileinfo.tar.xz
Source177:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltximg.doc.tar.xz
Source178:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ltximg.tar.xz
Source179:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lua2dox.doc.tar.xz
Source180:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lua2dox.tar.xz
Source181:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luaotfload.doc.tar.xz
Source182:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luaotfload.tar.xz
Source183:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luatex.doc.tar.xz
Source184:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/luatex.tar.xz
Source185:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lwarp.doc.tar.xz
Source186:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/lwarp.tar.xz
Source187:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/make4ht.doc.tar.xz
Source188:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/make4ht.tar.xz
Source189:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makedtx.doc.tar.xz
Source190:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makedtx.tar.xz
Source191:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makeindex.doc.tar.xz
Source192:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/makeindex.tar.xz
Source193:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/match_parens.doc.tar.xz
Source194:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/match_parens.tar.xz
Source195:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathspic.doc.tar.xz
Source196:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mathspic.tar.xz
Source197:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metafont.doc.tar.xz
Source198:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metafont.tar.xz
Source199:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metapost.doc.tar.xz
Source200:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/metapost.tar.xz
Source201:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mex.doc.tar.xz
Source202:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mex.tar.xz
Source203:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mf2pt1.doc.tar.xz
Source204:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mf2pt1.tar.xz
Source205:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mflua.tar.xz
Source206:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mfware.doc.tar.xz
Source207:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mfware.tar.xz
Source208:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mkgrkindex.doc.tar.xz
Source209:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mkgrkindex.tar.xz
Source210:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mkjobtexmf.doc.tar.xz
Source211:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mkjobtexmf.tar.xz
Source212:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mkpic.doc.tar.xz
Source213:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mkpic.tar.xz
Source214:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mltex.doc.tar.xz
Source215:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mltex.tar.xz
Source216:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mptopdf.doc.tar.xz
Source217:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/mptopdf.tar.xz
Source218:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/m-tx.doc.tar.xz
Source219:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/m-tx.tar.xz
Source220:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multibibliography.doc.tar.xz
Source221:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/multibibliography.tar.xz
Source222:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/musixtex.doc.tar.xz
Source223:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/musixtex.tar.xz
Source224:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/musixtnt.doc.tar.xz
Source225:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/musixtnt.tar.xz
Source226:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/omegaware.doc.tar.xz
Source227:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/patgen.doc.tar.xz
Source228:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/patgen.tar.xz
Source229:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pax.doc.tar.xz
Source230:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pax.tar.xz
Source231:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfbook2.doc.tar.xz
Source232:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfbook2.tar.xz
Source233:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfcrop.doc.tar.xz
Source234:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfcrop.tar.xz
Source235:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfjam.doc.tar.xz
Source236:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfjam.tar.xz
Source237:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdflatexpicscale.doc.tar.xz
Source238:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdflatexpicscale.tar.xz
Source239:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdftex.doc.tar.xz
Source240:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdftex.tar.xz
Source241:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdftools.doc.tar.xz
Source242:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdftools.tar.xz
Source243:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfxup.doc.tar.xz
Source244:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pdfxup.tar.xz
Source245:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pedigree-perl.doc.tar.xz
Source246:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pedigree-perl.tar.xz
Source247:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/perltex.doc.tar.xz
Source248:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/perltex.tar.xz
Source249:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/petri-nets.doc.tar.xz
Source250:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/petri-nets.tar.xz
Source251:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pfarrei.doc.tar.xz
Source252:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pfarrei.tar.xz
Source253:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pkfix.doc.tar.xz
Source254:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pkfix-helper.doc.tar.xz
Source255:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pkfix-helper.tar.xz
Source256:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pkfix.tar.xz
Source257:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pmxchords.doc.tar.xz
Source258:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pmxchords.tar.xz
Source259:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pmx.doc.tar.xz
Source260:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pmx.tar.xz
Source261:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ps2pk.doc.tar.xz
Source262:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ps2pk.tar.xz
Source263:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst2pdf.doc.tar.xz
Source264:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst2pdf.tar.xz
Source265:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pstools.tar.xz
Source266:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-pdf.doc.tar.xz
Source267:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pst-pdf.tar.xz
Source268:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ptex2pdf.doc.tar.xz
Source269:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ptex2pdf.tar.xz
Source270:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ptex.doc.tar.xz
Source271:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ptex-fontmaps.doc.tar.xz
Source272:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ptex-fontmaps.tar.xz
Source273:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ptex.tar.xz
Source274:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/purifyeps.doc.tar.xz
Source275:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/purifyeps.tar.xz
Source276:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pygmentex.doc.tar.xz
Source277:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pygmentex.tar.xz
Source278:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pythontex.doc.tar.xz
Source279:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/pythontex.tar.xz
Source280:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rubik.doc.tar.xz
Source281:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/rubik.tar.xz
Source282:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/seetexk.doc.tar.xz
Source283:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/seetexk.tar.xz
Source284:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/splitindex.doc.tar.xz
Source285:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/splitindex.tar.xz
Source286:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/srcredact.doc.tar.xz
Source287:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/srcredact.tar.xz
Source288:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sty2dtx.doc.tar.xz
Source289:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/sty2dtx.tar.xz
Source290:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/svn-multi.doc.tar.xz
Source291:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/svn-multi.tar.xz
Source292:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/synctex.doc.tar.xz
Source293:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/synctex.tar.xz
Source294:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tetex.doc.tar.xz
Source295:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tetex.tar.xz
Source296:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex4ebook.doc.tar.xz
Source297:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex4ebook.tar.xz
Source298:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex4ht.doc.tar.xz
Source299:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex4ht.tar.xz
Source300:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texcount.doc.tar.xz
Source301:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texcount.tar.xz
Source302:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texdef.doc.tar.xz
Source303:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texdef.tar.xz
Source304:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texdiff.doc.tar.xz
Source305:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texdiff.tar.xz
Source306:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texdirflatten.doc.tar.xz
Source307:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texdirflatten.tar.xz
Source308:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texdoc.doc.tar.xz
Source309:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex.doc.tar.xz
Source310:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texdoc.tar.xz
Source311:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texdoctk.tar.xz
Source312:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texdoctk.doc.tar.xz
Source313:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texfot.doc.tar.xz
Source314:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texfot.tar.xz
Source315:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive.infra.doc.tar.xz
Source316:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive.infra.tar.xz
Source317:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texliveonfly.doc.tar.xz
Source318:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texliveonfly.tar.xz
Source319:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-scripts.doc.tar.xz
Source320:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texlive-scripts.tar.xz
Source321:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texloganalyser.doc.tar.xz
Source322:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texloganalyser.tar.xz
Source323:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texosquery.doc.tar.xz
Source324:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texosquery.tar.xz
Source325:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texsis.doc.tar.xz
Source326:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texsis.tar.xz
Source327:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tex.tar.xz
Source328:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texware.doc.tar.xz
Source329:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/texware.tar.xz
Source330:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thumbpdf.doc.tar.xz
Source331:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/thumbpdf.tar.xz
Source332:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tie.doc.tar.xz
Source333:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tie.tar.xz
Source334:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tpic2pdftex.doc.tar.xz
Source335:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/tpic2pdftex.tar.xz
Source336:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ttfutils.doc.tar.xz
Source337:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ttfutils.tar.xz
Source338:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typeoutfileinfo.doc.tar.xz
Source339:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/typeoutfileinfo.tar.xz
Source340:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ulqda.doc.tar.xz
Source341:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ulqda.tar.xz
Source342:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uplatex.doc.tar.xz
Source343:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/uptex.doc.tar.xz
Source344:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/urlbst.doc.tar.xz
Source345:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/urlbst.tar.xz
Source346:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/velthuis.doc.tar.xz
Source347:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/velthuis.tar.xz
Source348:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vlna.doc.tar.xz
Source349:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vpe.doc.tar.xz
Source350:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/vpe.tar.xz
Source351:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/web.doc.tar.xz
Source352:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/web.tar.xz
Source353:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wordcount.doc.tar.xz
Source354:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/wordcount.tar.xz
Source355:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xdvi.doc.tar.xz
Source356:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xdvi.tar.xz
Source357:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetex.doc.tar.xz
Source358:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xetex.tar.xz
Source359:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xindy.doc.tar.xz
Source360:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xindy.tar.xz
Source361:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xmltex.doc.tar.xz
Source362:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/xmltex.tar.xz
Source363:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yplan.doc.tar.xz
Source364:      http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/yplan.tar.xz
Patch0001:      tl-kpfix.patch
Patch0002:      tl-format.patch
Patch0005:      texlive-20180414-synctex-version.patch
Patch0006:      texlive-base-CVE-2018-17407.patch
Patch0007:      fix-build-error-when-srctopdf-is-ok.patch
Patch0008:      remove-support-of-poppler.patch

BuildRequires:  xz libXaw-devel libXi-devel ncurses-devel bison flex file perl(Digest::MD5) texinfo gcc-c++
BuildRequires:  gd-devel freetype-devel libpng-devel zlib-devel
BuildRequires:  zziplib-devel libicu-devel cairo-devel harfbuzz-devel perl-generators pixman-devel graphite2-devel
BuildRequires:  libpaper-devel autoconf automake libtool libgs-devel
BuildRequires:  gmp-devel mpfr-devel python3-devel chrpath
Provides:       texlive-cjk-gs-integrate = %{epoch}:20180414-%{release}
Obsoletes:      texlive-cjk-gs-integrate <= 7:20170520
Provides:       tex-cjk-gs-integrate = %{epoch}:20180414-%{release}
Obsoletes:      tex-cjk-gs-integrate <= 7:20170520
Provides:       texlive-cjk-gs-integrate-bin = %{epoch}:20180414-%{release}
Provides:       tex-cjk-gs-integrate-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-cjk-gs-integrate-bin <= 7:20170520
Obsoletes:      tex-cjk-gs-integrate-bin <= 7:20170520
Provides:       texlive-cjk-gs-integrate-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-cjk-gs-integrate-doc <= 7:20170520

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.

%package -n texlive-a2ping
Provides:       tex-a2ping = %{epoch}:20180414-%{release}
Provides:       texlive-a2ping-bin = %{epoch}:20180414-%{release}
Provides:       tex-a2ping-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-a2ping-bin < 7:20170520
License:        GPL+
Summary:        Advanced PS, PDF, EPS converter
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-a2ping
a2ping is a Perl script command line utility written for Unix
that converts many raster image and vector graphics formats to
EPS or PDF and other page description formats. Accepted input
file formats are: PS (PostScript), EPS, PDF, PNG, JPEG, TIFF,
PNM, BMP, GIF, LBM, XPM, PCX, TGA. Accepted output formats are:
EPS, PCL5, PDF, PDF1, PBM, PGM, PPM, PS, markedEPS, markedPS,
PNG, XWD, BMP, TIFF, JPEG, GIF, XPM. a2ping delegates the low-
level work to Ghostscript (GS), pdftops and sam2p. a2ping fixes
many glitches during the EPS to EPS conversion, so its output
is often more compatible and better embeddable than its input.

%package -n texlive-accfonts
Provides:       tex-accfonts = %{epoch}:20180414-%{release}
Provides:       texlive-accfonts-bin = %{epoch}:20180414-%{release}
Provides:       tex-accfonts-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-accfonts-bin < 7:20170520
Provides:       tex-accfonts-doc = %{epoch}:20180414-%{release}
Provides:       texlive-accfonts-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-accfonts-doc < 7:20170520
License:        GPL+
Summary:        Utilities to derive new fonts from existing ones
Requires:       texlive-base texlive-kpathsea
Provides:       tex(CSX.def) = %{epoch}:20180414-%{release}
Provides:       tex(ISO-Latin1.def) = %{epoch}:20180414-%{release}
Provides:       tex(ISO-Latin2.def) = %{epoch}:20180414-%{release}
Provides:       tex(IndUni_Omega.def) = %{epoch}:20180414-%{release}
Provides:       tex(Norman.def) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-accfonts
The accfonts package contains three utilities to permit easy
manipulation of fonts, in particular the creation of unusual
accented characters. Mkt1font works on Adobe Type 1 fonts,
vpl2vpl works on TeX virtual fonts and vpl2ovp transforms a TeX
font to an Omega one. All three programs read in a font (either
the font itself or a property list), together with a simple
definition file containing lines such as '128 z acute'; they
then write out a new version of the font with the requested new
characters in the numerical slots specified. Great care is
taken over the positioning of accents, and over the provision
of kerning information for new characters; mkt1font also
generates suitable "hints" to enhance quality at small sizes or
poor resolutions. The programs are written in Perl.

%package -n texlive-adhocfilelist
Provides:       tex-adhocfilelist = %{epoch}:20180414-%{release}
Provides:       texlive-adhocfilelist-bin = %{epoch}:20180414-%{release}
Provides:       tex-adhocfilelist-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-adhocfilelist-bin < 7:20170520
Provides:       tex-adhocfilelist-doc = %{epoch}:20180414-%{release}
Provides:       texlive-adhocfilelist-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-adhocfilelist-doc < 7:20170520
License:        LPPL
Summary:        '\listfiles' entries from the command line
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-adhocfilelist
The package provides a Unix shell script to display a list of
LaTeX \Provides...-command contexts on screen. Provision is
made for controlling the searches that the package does. The
package was developed on a Unix-like system, using (among other
things) the gnu variant of the find command.

%package -n texlive-afm2pl
Provides:       tex-afm2pl = %{epoch}:20180414-%{release}
Provides:       texlive-afm2pl-bin = %{epoch}:20180414-%{release}
Provides:       tex-afm2pl-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-afm2pl-bin < 7:20170520
License:        LPPL
Summary:        afm2pl package
Requires:       texlive-base texlive-kpathsea
Provides:       tex(afm2pl-ot1.enc) = %{epoch}:20180414-%{release}
Provides:       tex(afm2pl-ot1ital.enc) = %{epoch}:20180414-%{release}
Provides:       tex(afm2pl-ot1tt.enc) = %{epoch}:20180414-%{release}
Provides:       tex(afm2pl-texnanlc.enc) = %{epoch}:20180414-%{release}
Provides:       tex(afm2pl-texnanuc.enc) = %{epoch}:20180414-%{release}
Provides:       tex(makesc8y.tex) = %{epoch}:20180414-%{release}

%description -n texlive-afm2pl
afm2pl package.

%package -n texlive-aleph
Provides:       tex-aleph = %{epoch}:20180414-%{release}
Provides:       texlive-aleph-bin = %{epoch}:20180414-%{release}
Provides:       tex-aleph-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-aleph-bin < 7:20170520
Provides:       tex-aleph-doc = %{epoch}:20180414-%{release}
Provides:       texlive-aleph-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-aleph-doc < 7:20170520
Summary:        Extended TeX
Requires:       texlive-base texlive-kpathsea texlive-tetex
Requires(post,postun): coreutils
Requires:       texlive-latex texlive-plain texlive-lambda texlive-cm texlive-hyphen-base texlive-knuth-lib
Requires:       texlive-knuth-lib texlive-antomega texlive-latex-fonts texlive-omega

%description -n texlive-aleph
An development of omega, using most of the extensions of TeX
itself developed for e-TeX.

%package -n texlive-amstex
Provides:       tex-amstex = %{epoch}:20180414-%{release}
Provides:       texlive-amstex-bin = %{epoch}:20180414-%{release}
Provides:       tex-amstex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-amstex-bin < 7:20170520
Provides:       tex-amstex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-amstex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-amstex-doc < 7:20170520
License:        LPPL
Summary:        American Mathematical Society plain TeX macros
Requires:       texlive-base texlive-kpathsea texlive-tetex
Requires(post,postun): coreutils
Requires:       texlive-tex texlive-amsfonts texlive-cm texlive-hyphen-base texlive-knuth-lib
Requires:       texlive-pdftex texlive-plain
Provides:       tex(amsppt.sty) = %{epoch}:20180414-%{release}
Provides:       tex(amsppt1.tex) = %{epoch}:20180414-%{release}
Provides:       tex(amstex.bug) = %{epoch}:20180414-%{release}
Provides:       tex(amstex.tex) = %{epoch}:20180414-%{release}
Provides:       tex(amstex.ini) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-amstex
AMSTeX is a TeX macro package, originally written by Michael
Spivak for the American Mathematical Society (AMS) during 1983-
1985 and is described in the book 'The Joy of TeX'. It is based
on Plain TeX, and provides many features for producing more
professional-looking maths formulas with less burden on
authors. More recently, the focus of attention has switched to
amslatex, but AMSTeX remains as a working system.

%package -n texlive-arara
Provides:       tex-arara = %{epoch}:20180414-%{release}
Provides:       texlive-arara-bin = %{epoch}:20180414-%{release}
Provides:       tex-arara-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-arara-bin < 7:20170520
Provides:       tex-arara-doc = %{epoch}:20180414-%{release}
Provides:       texlive-arara-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-arara-doc < 7:20170520
License:        BSD
Summary:        Automation of LaTeX compilation
Requires:       texlive-base texlive-kpathsea
Provides:       bundled(slf4j) = 1.6.4 bundled(apache-commons-collections) = 3.2.1
Provides:       bundled(apache-commons-exec) = 1.1 bundled(apache-commons-lang3) = 3.1
Provides:       bundled(apache-commons-cli) = 1.2 bundled(mvel2) = 2.0.19
Provides:       bundled(snakeyaml) = 1.11 bunbled(logback) = 1.0.1
BuildArch:      noarch

%description -n texlive-arara
Arara is comparable with other well-known compilation tools
like latexmk and rubber. The key difference is that that arara
determines its actions from metadata in the source code, rather
than relying on indirect resources, such as log file analysis.

%package -n texlive-authorindex
Provides:       tex-authorindex = %{epoch}:20180414-%{release}
Provides:       texlive-authorindex-bin = %{epoch}:20180414-%{release}
Provides:       tex-authorindex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-authorindex-bin < 7:20170520
Provides:       tex-authorindex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-authorindex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-authorindex-doc < 7:20170520
License:        LPPL
Summary:        Index citations by author names
Requires:       texlive-base texlive-kpathsea
Provides:       tex(authorindex.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-authorindex
This package allows the user to create an index of all authors
cited in a LaTeX document. Each author entry in the index
contains the pages where these citations occur. Alternatively,
the package can list the labels of the citations that appear in
the references rather than the text pages. The package relies
on BibTeX being used to handle citations. Additionally, it
requires Perl (version 5 or higher).

%package -n texlive-autosp
Provides:       tex-autosp = %{epoch}:20180414-%{release}
Provides:       texlive-autosp-bin = %{epoch}:20180414-%{release}
Provides:       tex-autosp-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-autosp-bin < 7:20170520
Provides:       tex-autosp-doc = %{epoch}:20180414-%{release}
Provides:       texlive-autosp-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-autosp-doc < 7:20170520
License:        GPLv2
Summary:        A Preprocessor that generates note-spacing commands for MusiXTeX scores
Requires:       texlive-base

%description -n texlive-autosp
This program simplifies the creation of MusiXTeX scores by
converting (non-standard) commands of the form \anotes ... \en
into one or more conventional note-spacing commands, as
determined by the note values themselves, with \sk spacing
commands inserted as necessary. The coding for an entire
measure can be entered one part at a time, without concern for
note-spacing changes within the part or spacing requirements of
other parts. For example, \anotes\qa J\qa K&\ca l\qa m\ca n\en
generates \Notes\qa J\sk\qa K\sk&\ca l\qa m\sk\ca n\en .

%package -n texlive-axodraw2
Provides:       tex-axodraw2 = %{epoch}:20180414-%{release}
Provides:       texlive-axodraw2-bin = %{epoch}:20180414-%{release}
License:        GPLv3
Summary:        Feynman diagrams in a LaTeX document
Requires:       texlive-base texlive-kpathsea
Provides:       tex(axodraw2.sty) = %{epoch}:20180414-%{release}

%description -n texlive-axodraw2
This package defines macros for drawing Feynman graphs in LaTeX
documents. It is an important update of the axodraw package,
but since it is not completely backwards compatible, we have
given the style file a changed name. Many new features have
been added, with new types of line, and much more flexibility
in their properties. In addition, it is now possible to use
axodraw2 with pdfLaTeX, as well as with the LaTeX-dvips method.
However with pdfLaTeX (and also LuaLaTeX and XeLaTeX), an
external program, axohelp, is used to perform the geometrical
calculations needed for the pdf code inserted in the output
file. The processing involves a run of pdfLaTeX, a run of
axohelp, and then another run of pdfLaTeX.

%package -n texlive-bib2gls
Provides:       tex-bib2gls = %{epoch}:20180414-%{release}
Provides:       texlive-bib2gls-bin = %{epoch}:20180414-%{release}
License:        GPLv3+
Summary:        Convert .bib files to glossaries-extra.sty resource files
Requires:       texlive-base
BuildArch:      noarch

%description -n texlive-bib2gls
This Java command line application may be used to extract
glossary information stored in a .bib file and convert it into
glossary entry definition commands. This application should be
used with glossaries-extra.sty's 'record' package option. It
performs two functions in one: selects entries according to
records found in the .aux file (similar to bibtex),
hierarchically sorts entries and collates location lists
(similar to makeindex or xindy). The glossary entries can then
be managed in a system such as JabRef, and only the entries
that are actually required will be defined, reducing the
resources required by TeX. The supplementary application
convertgls2bib can be used to convert existing .tex files
containing definitions (\newglossaryentry etc.) to the .bib
format required by bib2gls.

%package -n texlive-bibexport
Provides:       tex-bibexport = %{epoch}:20180414-%{release}
Provides:       texlive-bibexport-bin = %{epoch}:20180414-%{release}
Provides:       tex-bibexport-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-bibexport-bin < 7:20170520
Provides:       tex-bibexport-doc = %{epoch}:20180414-%{release}
Provides:       texlive-bibexport-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-bibexport-doc < 7:20170520
License:        LPPL 1.3
Summary:        Extract a BibTeX file based on a .aux file
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-bibexport
A Bourne shell script that uses BibTeX to extract bibliography
entries that are \cite'd in a document. It can also expand a
BibTeX file, expanding the abbreviations (other than the built-
in ones like month names) and followig the cross-references.

%package -n texlive-bibtex
Provides:       tex-bibtex = %{epoch}:20180414-%{release}
Provides:       texlive-bibtex-bin = %{epoch}:20180414-%{release}
Provides:       tex-bibtex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-bibtex-bin < 7:20170520
Provides:       tex-bibtex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-bibtex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-bibtex-doc < 7:20170520
License:        Knuth
Summary:        Process bibliographies for LaTeX, etc
Requires:       texlive-base texlive-kpathsea
Provides:       tex(apalike.sty) = %{epoch}:20180414-%{release}
Provides:       tex(apalike.tex) = %{epoch}:20180414-%{release}

%description -n texlive-bibtex
BibTeX allows the user to store his citation data in generic
form, while printing citations in a document in the form
specified by a BibTeX style, to be specified in the document
itself (one often needs a LaTeX citation-style package, such as
natbib as well). BibTeX itself is an ASCII-only program; there
is, however, a version that copes with 8-bit character sets.
However, BibTeX's facilities rapidly run out as one moves away
from simple ASCII (for example, in the various national sorting
rules for languages expressed in different parts of ISO-8859 --
the "ISO Latin" series). For more flexibility, the user is
urged to consider using biber with biblatex to typeset its
output. In fact, it is best to avoid BibTeX in favour of biber
and biblatex, if at all possible.

%package -n texlive-bibtexu
Provides:       tex-bibtexu = %{epoch}:20180414-%{release}
Provides:       texlive-bibtexu-bin = %{epoch}:20180414-%{release}
Provides:       tex-bibtexu-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-bibtexu-bin < 7:20170520
Provides:       tex-bibtexu-doc = %{epoch}:20180414-%{release}
Provides:       texlive-bibtexu-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-bibtexu-doc < 7:20170520
License:        LPPL
Summary:        bibtexu package
Requires:       texlive-base texlive-kpathsea

%description -n texlive-bibtexu
bibtexu package.

%package -n texlive-bibtex8
Provides:       tex-bibtex8 = %{epoch}:20180414-%{release}
Provides:       texlive-bibtex8-bin = %{epoch}:20180414-%{release}
Provides:       tex-bibtex8-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-bibtex8-bin < 7:20170520
Provides:       tex-bibtex8-doc = %{epoch}:20180414-%{release}
Provides:       texlive-bibtex8-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-bibtex8-doc < 7:20170520
License:        GPL+
Summary:        A fully 8-bit adaptation of BibTeX 0.99
Requires:       texlive-base texlive-kpathsea

%description -n texlive-bibtex8
An enhanced, portable C version of BibTeX. Enhanced by
conversion to "big" (32-bit) capacity, addition of run-time
selectable capacity and 8-bit support extensions. National
character set and sorting order are controlled by an external
configuration file. Various examples are included.

%package -n texlive-bundledoc
Provides:       tex-bundledoc = %{epoch}:20180414-%{release}
Provides:       texlive-bundledoc-bin = %{epoch}:20180414-%{release}
Provides:       tex-bundledoc-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-bundledoc-bin < 7:20170520
Provides:       tex-bundledoc-doc = %{epoch}:20180414-%{release}
Provides:       texlive-bundledoc-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-bundledoc-doc < 7:20170520
License:        LPPL
Summary:        Bundle together all the files needed to build a LaTeX document
Requires:       texlive-base texlive-kpathsea
Provides:       tex(miktex.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(texlive-unix-arlatex.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(texlive-unix.cfg) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-bundledoc
The bundledoc package is a post-processor for the snapshot
package that bundles together all the classes, packages and
files needed to build a given LaTeX document. It reads the .dep
file that snapshot produces, finds each of the files mentioned
therein, and archives them into a single .tar.gz (or .zip, or
whatever) file, suitable for moving across systems,
transmitting to a colleague, etc. A script, arlatex, provides
an alternative "archiving" mechanism, creating a single LaTeX
file that contains all of the ancillary files of a LaTeX
document, together with the document itself, using the
filecontents* environment.

%package -n texlive-cachepic
Provides:       tex-cachepic = %{epoch}:20180414-%{release}
Provides:       texlive-cachepic-bin = %{epoch}:20180414-%{release}
Provides:       tex-cachepic-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-cachepic-bin < 7:20170520
Provides:       tex-cachepic-doc = %{epoch}:20180414-%{release}
Provides:       texlive-cachepic-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-cachepic-doc < 7:20170520
License:        LPPL 1.3
Summary:        Convert document fragments into graphics
Requires:       texlive-base texlive-kpathsea tex(graphicx.sty) tex(verbatim.sty)
Provides:       tex(cachepic.sty) = %{epoch}:20180414-%{release}
Provides:       tex(prcachepic.def) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-cachepic
The bundle simplifies and automates conversion of document
fragments into external EPS or PDF files. The bundle consists
of two parts: a LaTeX package that implements a document level
interface, and a command line tool (written in lua) that
generates the external graphics.

%package -n texlive-checkcites
Provides:       tex-checkcites = %{epoch}:20180414-%{release}
Provides:       texlive-checkcites-bin = %{epoch}:20180414-%{release}
Provides:       tex-checkcites-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-checkcites-bin < 7:20170520
Provides:       tex-checkcites-doc = %{epoch}:20180414-%{release}
Provides:       texlive-checkcites-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-checkcites-doc < 7:20170520
License:        LPPL 1.3
Summary:        Check citation commands in a document
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-checkcites
The package provides a lua script written for the sole purpose
of detecting undefined and unused references from LaTeX
auxiliary or bibliography files.

%package -n texlive-checklistings
Provides:       tex-checklistings = %{epoch}:20180414-%{release}
Provides:       texlive-checklistings-bin = %{epoch}:20180414-%{release}
Provides:       tex-checklistings-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-checklistings-bin < 7:20170520
Provides:       tex-checklistings-doc = %{epoch}:20180414-%{release}
Provides:       texlive-checklistings-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-checklistings-doc < 7:20170520
License:        LPPL 1.2
Summary:        Pass verbatim contents through a compiler and reincorporate the resulting output
Requires:       texlive-base texlive-kpathsea tex(keyval.sty) tex(kvoptions.sty) tex(fancyvrb.sty)
Requires:       tex(color.sty) tex(listings.sty)
Provides:       tex(checklistings.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-checklistings
This package augments the fancyvrb and listings packages to
allow the source code they contain to be checked by an external
tool (like a compiler). The external tool's messages can be
automatically reincorporated into the original document. The
package does not focus on a specific programming language, but
it is designed to work well with languages and compilers in the
ML family.

%package -n texlive-chktex
Provides:       tex-chktex = %{epoch}:20180414-%{release}
Provides:       texlive-chktex-bin = %{epoch}:20180414-%{release}
Provides:       tex-chktex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-chktex-bin < 7:20170520
Provides:       tex-chktex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-chktex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-chktex-doc < 7:20170520
License:        GPL+
Summary:        Check for errors in LaTeX documents
Requires:       texlive-base texlive-kpathsea

%description -n texlive-chktex
The program reports typographic and other errors in LaTeX
documents. Filters are also provided for checking the LaTeX
parts of CWEB documents.


%package -n texlive-cjkutils
Provides:       tex-cjkutils = %{epoch}:20180414-%{release}
Provides:       texlive-cjkutils-bin = %{epoch}:20180414-%{release}
Provides:       tex-cjkutils-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-cjkutils-bin < 7:20170520
License:        LPPL
Summary:        cjkutils package
Requires:       texlive-base texlive-kpathsea
Provides:       tex(b5ka12.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(b5kr12.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(b5so12.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(c1so12.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(c2so12.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(c3so12.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(c4so12.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(c5so12.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(c6so12.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(c7so12.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(csso12.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(gsfs14.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(j2so12.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(jsso12.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(ksso17.cfg) = %{epoch}:20180414-%{release}

%description -n texlive-cjkutils
cjkutils package.

%package -n texlive-context
Provides:       tex-context = %{epoch}:20180414-%{release}
Provides:       texlive-context-bin = %{epoch}:20180414-%{release}
Provides:       tex-context-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-context-bin < 7:20170520
Provides:       tex-context-doc = %{epoch}:20180414-%{release}
Provides:       texlive-context-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-context-doc < 7:20170520
License:        GPL+ or LPPL
Summary:        The ConTeXt macro package
Requires:       texlive-base texlive-kpathsea texlive-tetex texlive-metapost
Requires(post,postun): coreutils
Requires:       texlive-pdftex texlive-xetex texlive-luatex texlive-lm texlive-lm-math texlive-amsfonts
Requires:       texlive-manfnt-font texlive-mflogo-font texlive-stmaryrd texlive-mptopdf
Requires:       ruby tex(pstricks.sty)
Requires:       tex(pst-plot.sty)
Provides:       tex(notepad++.ini) = %{epoch}:20180414-%{release}
Provides:       tex(texworks-setup.ini) = %{epoch}:20180414-%{release}
Provides:       tex(tools.ini) = %{epoch}:20180414-%{release}
Provides:       tex(TeXworks.ini) = %{epoch}:20180414-%{release}
Provides:       tex(scite-context-readme.tex) = %{epoch}:20180414-%{release}
Provides:       tex(type-buy.dat) = %{epoch}:20180414-%{release}
Provides:       tex(type-fsf.dat) = %{epoch}:20180414-%{release}
Provides:       tex(type-ghz.dat) = %{epoch}:20180414-%{release}
Provides:       tex(type-tmf.dat) = %{epoch}:20180414-%{release}
Provides:       tex(contnav.afm) = %{epoch}:20180414-%{release}
Provides:       tex(cmin.enc) = %{epoch}:20180414-%{release}
Provides:       tex(cmit.enc) = %{epoch}:20180414-%{release}
Provides:       tex(cmitt.enc) = %{epoch}:20180414-%{release}
Provides:       tex(cmrm.enc) = %{epoch}:20180414-%{release}
Provides:       tex(cmsc.enc) = %{epoch}:20180414-%{release}
Provides:       tex(cmtt.enc) = %{epoch}:20180414-%{release}
Provides:       tex(ec-2004.enc) = %{epoch}:20180414-%{release}
Provides:       tex(q-8r.enc) = %{epoch}:20180414-%{release}
Provides:       tex(teff-trinite.enc) = %{epoch}:20180414-%{release}
Provides:       tex(contnav.map) = %{epoch}:20180414-%{release}
Provides:       tex(8r-base.map) = %{epoch}:20180414-%{release}
Provides:       tex(ec-base.map) = %{epoch}:20180414-%{release}
Provides:       tex(ec-os-public-lm.map) = %{epoch}:20180414-%{release}
Provides:       tex(mkiv-base.map) = %{epoch}:20180414-%{release}
Provides:       tex(mkiv-px.map) = %{epoch}:20180414-%{release}
Provides:       tex(mkiv-tx.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-adobe-euro.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-ams-base.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-ams-cmr.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-ams-euler.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-base.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-context-symbol.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-dummy.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-empty.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-micropress-informal.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-public-csr.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-public-lm.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-public-plr.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-public-vnr.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-vogel-symbol.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-wasy.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-youngryu-px.map) = %{epoch}:20180414-%{release}
Provides:       tex(original-youngryu-tx.map) = %{epoch}:20180414-%{release}
Provides:       tex(qx-base.map) = %{epoch}:20180414-%{release}
Provides:       tex(qx-os-public-lm.map) = %{epoch}:20180414-%{release}
Provides:       tex(t5-base.map) = %{epoch}:20180414-%{release}
Provides:       tex(t5-os-public-lm.map) = %{epoch}:20180414-%{release}
Provides:       tex(texnansi-base.map) = %{epoch}:20180414-%{release}
Provides:       tex(texnansi-os-public-lm.map) = %{epoch}:20180414-%{release}
Provides:       tex(tlig.map) = %{epoch}:20180414-%{release}
Provides:       tex(contnav.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(contnav.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(bidi-symbols.tex) = %{epoch}:20180414-%{release}
Provides:       tex(demo-symbols.tex) = %{epoch}:20180414-%{release}
Provides:       tex(export-example.tex) = %{epoch}:20180414-%{release}
Provides:       tex(m-cweb.tex) = %{epoch}:20180414-%{release}
Provides:       tex(m-datastrc.tex) = %{epoch}:20180414-%{release}
Provides:       tex(m-educat.tex) = %{epoch}:20180414-%{release}
Provides:       tex(m-format.tex) = %{epoch}:20180414-%{release}
Provides:       tex(m-layout.tex) = %{epoch}:20180414-%{release}
Provides:       tex(m-narrowtt.tex) = %{epoch}:20180414-%{release}
Provides:       tex(m-newmat.tex) = %{epoch}:20180414-%{release}
Provides:       tex(m-pictex.tex) = %{epoch}:20180414-%{release}
Provides:       tex(m-streams.tex) = %{epoch}:20180414-%{release}
Provides:       tex(m-subsub.tex) = %{epoch}:20180414-%{release}
Provides:       tex(metatex.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mtx-context-arrange.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mtx-context-combine.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mtx-context-common.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mtx-context-copy.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mtx-context-ideas.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mtx-context-listing.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mtx-context-markdown.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mtx-context-precache.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mtx-context-select.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mtx-context-sql.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mtx-context-timing.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mtx-context-xml.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-abr-01.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-abr-02.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-abr-03.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-abr-04.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-cdr-01.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-faq-00.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-faq-01.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-faq-02.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-faq-03.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-mag-01.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-00.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-01.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-02.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-03.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-04.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-05.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-06.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-07.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-08.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-09.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-10.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-11.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-12.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-13.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-14.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-15.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-16.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-18.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-19.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-22.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-23.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-26.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-27.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-50.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-61.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-62.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-63.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-64.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-66.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-67.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-68.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-93.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-pre-96.tex) = %{epoch}:20180414-%{release}
Provides:       tex(s-ptj-01.tex) = %{epoch}:20180414-%{release}
Provides:       tex(status-mkiv.tex) = %{epoch}:20180414-%{release}
Provides:       tex(supp-mis.tex) = %{epoch}:20180414-%{release}
Provides:       tex(supp-mpe.tex) = %{epoch}:20180414-%{release}
Provides:       tex(supp-pdf.tex) = %{epoch}:20180414-%{release}
Provides:       tex(x-dir-01.tex) = %{epoch}:20180414-%{release}
Provides:       tex(bibl-ams.tex) = %{epoch}:20180414-%{release}
Provides:       tex(bibl-apa-de.tex) = %{epoch}:20180414-%{release}
Provides:       tex(bibl-apa-fr.tex) = %{epoch}:20180414-%{release}
Provides:       tex(bibl-apa-it.tex) = %{epoch}:20180414-%{release}
Provides:       tex(bibl-apa.tex) = %{epoch}:20180414-%{release}
Provides:       tex(bibl-aps.tex) = %{epoch}:20180414-%{release}
Provides:       tex(bibl-num-fr.tex) = %{epoch}:20180414-%{release}
Provides:       tex(bibl-num.tex) = %{epoch}:20180414-%{release}
Provides:       tex(bibl-ssa.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mag-0000.tex) = %{epoch}:20180414-%{release}
Provides:       tex(setup-qr.tex) = %{epoch}:20180414-%{release}
Provides:       tex(aesop-de.tex) = %{epoch}:20180414-%{release}
Provides:       tex(bryson.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cervantes-es.tex) = %{epoch}:20180414-%{release}
Provides:       tex(darwin.tex) = %{epoch}:20180414-%{release}
Provides:       tex(davis.tex) = %{epoch}:20180414-%{release}
Provides:       tex(dawkins.tex) = %{epoch}:20180414-%{release}
Provides:       tex(demo-mps.tex) = %{epoch}:20180414-%{release}
Provides:       tex(demo-tex.tex) = %{epoch}:20180414-%{release}
Provides:       tex(demo-xml.tex) = %{epoch}:20180414-%{release}
Provides:       tex(douglas.tex) = %{epoch}:20180414-%{release}
Provides:       tex(hawking.tex) = %{epoch}:20180414-%{release}
Provides:       tex(khatt-ar.tex) = %{epoch}:20180414-%{release}
Provides:       tex(khatt-en.tex) = %{epoch}:20180414-%{release}
Provides:       tex(knuth.tex) = %{epoch}:20180414-%{release}
Provides:       tex(linden.tex) = %{epoch}:20180414-%{release}
Provides:       tex(lorem.tex) = %{epoch}:20180414-%{release}
Provides:       tex(materie.tex) = %{epoch}:20180414-%{release}
Provides:       tex(montgomery.tex) = %{epoch}:20180414-%{release}
Provides:       tex(quevedo-es.tex) = %{epoch}:20180414-%{release}
Provides:       tex(reich.tex) = %{epoch}:20180414-%{release}
Provides:       tex(sample.tex) = %{epoch}:20180414-%{release}
Provides:       tex(samples.tex) = %{epoch}:20180414-%{release}
Provides:       tex(thuan.tex) = %{epoch}:20180414-%{release}
Provides:       tex(tufte.tex) = %{epoch}:20180414-%{release}
Provides:       tex(ward.tex) = %{epoch}:20180414-%{release}
Provides:       tex(weisman.tex) = %{epoch}:20180414-%{release}
Provides:       tex(zapf.tex) = %{epoch}:20180414-%{release}
Provides:       tex(context-test.tex) = %{epoch}:20180414-%{release}
Provides:       tex(luatex-basics.tex) = %{epoch}:20180414-%{release}
Provides:       tex(luatex-fonts.tex) = %{epoch}:20180414-%{release}
Provides:       tex(luatex-languages.tex) = %{epoch}:20180414-%{release}
Provides:       tex(luatex-math.tex) = %{epoch}:20180414-%{release}
Provides:       tex(luatex-mplib.tex) = %{epoch}:20180414-%{release}
Provides:       tex(luatex-plain.tex) = %{epoch}:20180414-%{release}
Provides:       tex(luatex-preprocessor-test.tex) = %{epoch}:20180414-%{release}
Provides:       tex(luatex-preprocessor.tex) = %{epoch}:20180414-%{release}
Provides:       tex(luatex-swiglib-test.tex) = %{epoch}:20180414-%{release}
Provides:       tex(luatex-swiglib.tex) = %{epoch}:20180414-%{release}
Provides:       tex(luatex-test.tex) = %{epoch}:20180414-%{release}
Provides:       tex(m-ch-de.tex) = %{epoch}:20180414-%{release}
Provides:       tex(m-ch-en.tex) = %{epoch}:20180414-%{release}
Provides:       tex(m-ch-nl.tex) = %{epoch}:20180414-%{release}
Provides:       tex(m-ch-de.sty) = %{epoch}:20180414-%{release}
Provides:       tex(m-ch-en.sty) = %{epoch}:20180414-%{release}
Provides:       tex(m-ch-nl.sty) = %{epoch}:20180414-%{release}
Provides:       tex(m-pictex.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-context
A full featured, parameter driven macro package, which fully
supports advanced interactive documents. See the ConTeXt garden
for a wealth of support information.

%package -n texlive-convbkmk
Provides:       tex-convbkmk = %{epoch}:20180414-%{release}
Provides:       texlive-convbkmk-bin = %{epoch}:20180414-%{release}
Provides:       tex-convbkmk-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-convbkmk-bin < 7:20170520
Provides:       tex-convbkmk-doc = %{epoch}:20180414-%{release}
Provides:       texlive-convbkmk-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-convbkmk-doc < 7:20170520
License:        MIT
Summary:        Correct platex/uplatex bookmarks in PDF created with hyperref
Requires:       texlive-base texlive-kpathsea ruby
BuildArch:      noarch

%description -n texlive-convbkmk
The package provides a small Ruby script that corrects
bookmarks in PDF files created by platex/uplatex, using
hyperref.

%package -n texlive-crossrefware
Provides:       tex-crossrefware = %{epoch}:20180414-%{release}
Provides:       texlive-crossrefware-bin = %{epoch}:20180414-%{release}
Provides:       tex-crossrefware-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-crossrefware-bin < 7:20170520
Provides:       tex-crossrefware-doc = %{epoch}:20180414-%{release}
Provides:       texlive-crossrefware-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-crossrefware-doc < 7:20170520
License:        GPL+
Summary:        Scripts for working with crossref.org
BuildArch:      noarch

%description -n texlive-crossrefware
This bundle contains the following scripts: bibdoiadd.pl: add
DOI numbers to papers in a given bib file, bibzbladd.pl: add
Zbl numbers to papers in a given bib file, ltx2crossrefxml.pl:
a tool for the creation of XML files for submitting to the
parent site

%package -n texlive-cslatex
Provides:       tex-cslatex = %{epoch}:20180414-%{release}
Provides:       texlive-cslatex-bin = %{epoch}:20180414-%{release}
Provides:       tex-cslatex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-cslatex-bin < 7:20170520
License:        GPL+
Summary:        LaTeX support for Czech/Slovak typesetting
Requires:       texlive-base texlive-kpathsea texlive-latex texlive-pdftex texlive-tetex
Requires(post,postun): coreutils
Requires:       tex(czech.ldf) tex(slovak.ldf)
Provides:       tex(czech.sty) = %{epoch}:20180414-%{release}
Provides:       tex(fonttext.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(hyphen.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(il2cmdh.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2cmfib.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2cmfr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2cmr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2cmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2cmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2cmvtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2enc.def) = %{epoch}:20180414-%{release}
Provides:       tex(il2lcmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2lcmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(slovak.sty) = %{epoch}:20180414-%{release}
Provides:       tex(cspsfont.tex) = %{epoch}:20180414-%{release}
Provides:       tex(il2pag.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2pbk.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2pcr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2phv.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2phvn.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2pnc.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2ppl.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2ptm.fd) = %{epoch}:20180414-%{release}
Provides:       tex(il2pzc.fd) = %{epoch}:20180414-%{release}
Provides:       tex(nhelvet.sty) = %{epoch}:20180414-%{release}
Provides:       tex(ntimes.sty) = %{epoch}:20180414-%{release}
Provides:       tex(xl2pag.fd) = %{epoch}:20180414-%{release}
Provides:       tex(xl2pbk.fd) = %{epoch}:20180414-%{release}
Provides:       tex(xl2pcr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(xl2phv.fd) = %{epoch}:20180414-%{release}
Provides:       tex(xl2phvn.fd) = %{epoch}:20180414-%{release}
Provides:       tex(xl2pnc.fd) = %{epoch}:20180414-%{release}
Provides:       tex(xl2ppl.fd) = %{epoch}:20180414-%{release}
Provides:       tex(xl2ptm.fd) = %{epoch}:20180414-%{release}
Provides:       tex(xl2pzc.fd) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-cslatex
LaTeX support for Czech/Slovak typesetting

%package -n texlive-csplain
Provides:       tex-csplain = %{epoch}:20180414-%{release}
Provides:       texlive-csplain-bin = %{epoch}:20180414-%{release}
Provides:       tex-csplain-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-csplain-bin < 7:20170520
License:        GPLv2+
Summary:        Plain TeX multilanguage support
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-pdftex texlive-tetex
Requires(post,postun): coreutils
Requires:       texlive-tex
Provides:       tex(csenc-k.tex) = %{epoch}:20180414-%{release}
Provides:       tex(csenc-p.tex) = %{epoch}:20180414-%{release}
Provides:       tex(csenc-u.tex) = %{epoch}:20180414-%{release}
Provides:       tex(csenc-w.tex) = %{epoch}:20180414-%{release}
Provides:       tex(csfonts.tex) = %{epoch}:20180414-%{release}
Provides:       tex(csfontsm.tex) = %{epoch}:20180414-%{release}
Provides:       tex(czhyphen.tex) = %{epoch}:20180414-%{release}
Provides:       tex(extcode.tex) = %{epoch}:20180414-%{release}
Provides:       tex(fonttabs.tex) = %{epoch}:20180414-%{release}
Provides:       tex(il2code.tex) = %{epoch}:20180414-%{release}
Provides:       tex(plaina4.tex) = %{epoch}:20180414-%{release}
Provides:       tex(skhyphen.tex) = %{epoch}:20180414-%{release}
Provides:       tex(t1code.tex) = %{epoch}:20180414-%{release}
Provides:       tex(t1enc-u.tex) = %{epoch}:20180414-%{release}
Provides:       tex(ucode.tex) = %{epoch}:20180414-%{release}
Provides:       tex(uni-lcuc.tex) = %{epoch}:20180414-%{release}
Provides:       tex(ams-math.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cavantga.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cbookman.tex) = %{epoch}:20180414-%{release}
Provides:       tex(chars-8z.tex) = %{epoch}:20180414-%{release}
Provides:       tex(chelvet.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cncent.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cpalatin.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cs-adventor.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cs-all.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cs-antt.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cs-arev.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cs-bera.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cs-bonum.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cs-charter.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cs-cursor.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cs-heros.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cs-pagella.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cs-polta.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cs-schola.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cs-termes.tex) = %{epoch}:20180414-%{release}
Provides:       tex(ctimes.tex) = %{epoch}:20180414-%{release}
Provides:       tex(cyrchars.tex) = %{epoch}:20180414-%{release}
Provides:       tex(dcfonts.tex) = %{epoch}:20180414-%{release}
Provides:       tex(ecfonts.tex) = %{epoch}:20180414-%{release}
Provides:       tex(exchars.tex) = %{epoch}:20180414-%{release}
Provides:       tex(lmfonts.tex) = %{epoch}:20180414-%{release}
Provides:       tex(luafonts.tex) = %{epoch}:20180414-%{release}
Provides:       tex(ntx-math.tex) = %{epoch}:20180414-%{release}
Provides:       tex(tx-math.tex) = %{epoch}:20180414-%{release}
Provides:       tex(unifam.tex) = %{epoch}:20180414-%{release}
Provides:       tex(opmac-bib-iso690.tex) = %{epoch}:20180414-%{release}
Provides:       tex(opmac-bib-simple.tex) = %{epoch}:20180414-%{release}
Provides:       tex(opmac-bib.tex) = %{epoch}:20180414-%{release}
Provides:       tex(opmac-xetex.tex) = %{epoch}:20180414-%{release}
Provides:       tex(opmac.tex) = %{epoch}:20180414-%{release}
Provides:       tex(pdfuni.tex) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-csplain
CSplain is a small extension of basic Plain TeX macros, the
formats csplain and pdfcsplain can be generated. It supports:
hyphenation of words for 50+ languages, simple and powerfull
font loading system (various sizes of fonts), tex, pdftex,
xetex and luatex engines, math fonts simply loaded with full
amstex-like features, three internal encodings (IL2 for
Czech/Slovak languages, T1 for many languages with latin
alphabet and Unicode in new TeX engines), natural UTF-8 input
in pdfTeX using encTeX without any active characters, Czech and
Slovak special typesetting features. An important part of the
package is OPmac, which implements most of LaTeX's features
(sectioning, font selection, color, hyper reference and urls,
bibliography, index, toc, tables,etc.) by Plain TeX macros. The
OPmac macros can generate and bibliography without any external
program.

%package -n texlive-ctan-o-mat
Provides:       tex-ctan-o-mat = %{epoch}:20180414-%{release}
Provides:       texlive-ctan-o-mat-bin = %{epoch}:20180414-%{release}
License:        BSD
Summary:        Upload or validate a package for CTAN
Requires:       texlive-base texlive-kpathsea
Requires:       perl-interpreter
BuildArch:      noarch

%description -n texlive-ctan-o-mat
This program can be used to automate the upload of a package to
CTAN. The description of the package is contained in a
configuration file. The provided information is validated in
any case. If the validation succeeds and not only the
validation is requested, then the provided archive file will be
placed in the incoming area of the CTAN for further processing
by the CTAN team. In any case any finding during the validation
is reported at the end of the processing. Note that the
validation is the default and an official submission has to be
requested by an appropriate command line option. ctan-o-mat
requires an Internet connection to the CTAN server. Even the
validation retrieves the known attributes and the basic
constraints from the server.

%package -n texlive-ctanify
Provides:       tex-ctanify = %{epoch}:20180414-%{release}
Provides:       texlive-ctanify-bin = %{epoch}:20180414-%{release}
Provides:       tex-ctanify-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ctanify-bin < 7:20170520
Provides:       tex-ctanify-doc = %{epoch}:20180414-%{release}
Provides:       texlive-ctanify-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ctanify-doc < 7:20170520
License:        LPPL 1.3
Summary:        Prepare a package for upload to CTAN
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-ctanify
Given a list of filenames, ctanify creates a tarball (a .tar.gz
file) with the files laid out in CTAN's preferred structure.
The tarball additionally contains a ZIP (.zip) file with copies
of all files laid out in the standard TeX Directory Structure
(TDS), which may be used by those intending to install the
package, or by those who need to incorporate it in a
distribution. (The TDS ZIP file will be installed in the CTAN
install/ tree.)

%package -n texlive-ctanupload
Provides:       tex-ctanupload = %{epoch}:20180414-%{release}
Provides:       texlive-ctanupload-bin = %{epoch}:20180414-%{release}
Provides:       tex-ctanupload-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ctanupload-bin < 7:20170520
Provides:       tex-ctanupload-doc = %{epoch}:20180414-%{release}
Provides:       texlive-ctanupload-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ctanupload-doc < 7:20170520
License:        GPLv3+
Summary:        Support for users uploading to CTAN
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-ctanupload
The package provides a Perl script that allows the uploads of a
contribution to CTAN from the command line. The aim is to
simplify the release process for LaTeX package authors.

%package -n texlive-ctie
Provides:       tex-ctie = %{epoch}:20180414-%{release} texlive-ctie-bin = %{epoch}:20180414-%{release}
Provides:       tex-ctie-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ctie-bin < 7:20170520
License:        GPL+
Summary:        C version of tie (merging Web change files)
Requires:       texlive-base texlive-kpathsea

%description -n texlive-ctie
This is a version of tie converted for use with cweb.

%package -n texlive-cweb
Provides:       tex-cweb = %{epoch}:20180414-%{release} texlive-cweb-bin = %{epoch}:20180414-%{release}
Provides:       tex-cweb-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-cweb-bin < 7:20170520
Provides:       tex-cweb-doc = %{epoch}:20180414-%{release}
Provides:       texlive-cweb-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-cweb-doc < 7:20170520
License:        Knuth
Summary:        A Web system in C
Requires:       texlive-base texlive-kpathsea
Provides:       tex(cwebmac.tex) = %{epoch}:20180414-%{release}
Provides:       tex(pdfXcwebmac.tex) = %{epoch}:20180414-%{release}
Provides:       tex(pdfcwebmac.tex) = %{epoch}:20180414-%{release}
Provides:       tex(pdfdcwebmac.tex) = %{epoch}:20180414-%{release}
Provides:       tex(pdffcwebmac.tex) = %{epoch}:20180414-%{release}
Provides:       tex(pdficwebmac.tex) = %{epoch}:20180414-%{release}
Provides:       tex(pdfwebmac.tex) = %{epoch}:20180414-%{release}

%description -n texlive-cweb
The Cweb system is a system for Structured Software
Documentation (also known as Literate Programming) in the
programming language C.

%package -n texlive-cyrillic
Provides:       tex-cyrillic = %{epoch}:20180414-%{release}
Provides:       texlive-cyrillic-bin = %{epoch}:20180414-%{release}
Provides:       tex-cyrillic-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-cyrillic-bin < 7:20170520
Provides:       tex-cyrillic-doc = %{epoch}:20180414-%{release}
Provides:       texlive-cyrillic-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-cyrillic-doc < 7:20170520
Provides:       texlive-cyrillic-bin-bin = %{epoch}:20180414-%{release}
Provides:       tex-cyrillic-bin-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-cyrillic-bin-bin < 7:20170520
License:        LPPL 1.3
Summary:        Support for Cyrillic fonts in LaTeX
Requires:       texlive-base texlive-kpathsea
Requires:       tex(fontenc.sty)
Provides:       tex(cp1251.def) = %{epoch}:20180414-%{release}
Provides:       tex(cp855.def) = %{epoch}:20180414-%{release}
Provides:       tex(cp866.def) = %{epoch}:20180414-%{release}
Provides:       tex(cp866av.def) = %{epoch}:20180414-%{release}
Provides:       tex(cp866mav.def) = %{epoch}:20180414-%{release}
Provides:       tex(cp866nav.def) = %{epoch}:20180414-%{release}
Provides:       tex(cp866tat.def) = %{epoch}:20180414-%{release}
Provides:       tex(ctt.def) = %{epoch}:20180414-%{release}
Provides:       tex(dbk.def) = %{epoch}:20180414-%{release}
Provides:       tex(iso88595.def) = %{epoch}:20180414-%{release}
Provides:       tex(isoir111.def) = %{epoch}:20180414-%{release}
Provides:       tex(koi8-r.def) = %{epoch}:20180414-%{release}
Provides:       tex(koi8-ru.def) = %{epoch}:20180414-%{release}
Provides:       tex(koi8-u.def) = %{epoch}:20180414-%{release}
Provides:       tex(lcy.sty) = %{epoch}:20180414-%{release}
Provides:       tex(lcyccr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(lcycmbr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(lcycmdh.fd) = %{epoch}:20180414-%{release}
Provides:       tex(lcycmfib.fd) = %{epoch}:20180414-%{release}
Provides:       tex(lcycmfr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(lcycmr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(lcycmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(lcycmtl.fd) = %{epoch}:20180414-%{release}
Provides:       tex(lcycmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(lcycmvtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(lcydefs.tex) = %{epoch}:20180414-%{release}
Provides:       tex(lcyenc.def) = %{epoch}:20180414-%{release}
Provides:       tex(lcylcmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(lcylcmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(maccyr.def) = %{epoch}:20180414-%{release}
Provides:       tex(macukr.def) = %{epoch}:20180414-%{release}
Provides:       tex(mik.def) = %{epoch}:20180414-%{release}
Provides:       tex(mls.def) = %{epoch}:20180414-%{release}
Provides:       tex(mnk.def) = %{epoch}:20180414-%{release}
Provides:       tex(mos.def) = %{epoch}:20180414-%{release}
Provides:       tex(ncc.def) = %{epoch}:20180414-%{release}
Provides:       tex(ot2ccr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot2cmbr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot2cmdh.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot2cmfib.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot2cmfr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot2cmr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot2cmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot2cmtl.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot2cmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot2cmvtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot2enc.def) = %{epoch}:20180414-%{release}
Provides:       tex(ot2lcmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot2lcmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot2wlcyr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot2wlcyss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot2wncyr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot2wncyss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(pt154.def) = %{epoch}:20180414-%{release}
Provides:       tex(pt254.def) = %{epoch}:20180414-%{release}
Provides:       tex(t2accr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2acmbr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2acmdh.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2acmfib.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2acmfr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2acmr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2acmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2acmtl.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2acmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2acmvtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2aenc.def) = %{epoch}:20180414-%{release}
Provides:       tex(t2alcmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2alcmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2bccr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2bcmbr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2bcmdh.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2bcmfib.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2bcmfr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2bcmr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2bcmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2bcmtl.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2bcmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2bcmvtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2benc.def) = %{epoch}:20180414-%{release}
Provides:       tex(t2blcmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2blcmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2cccr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2ccmbr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2ccmdh.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2ccmfib.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2ccmfr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2ccmr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2ccmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2ccmtl.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2ccmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2ccmvtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2cenc.def) = %{epoch}:20180414-%{release}
Provides:       tex(t2clcmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t2clcmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(x2ccr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(x2cmbr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(x2cmdh.fd) = %{epoch}:20180414-%{release}
Provides:       tex(x2cmfib.fd) = %{epoch}:20180414-%{release}
Provides:       tex(x2cmfr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(x2cmr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(x2cmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(x2cmtl.fd) = %{epoch}:20180414-%{release}
Provides:       tex(x2cmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(x2cmvtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(x2enc.def) = %{epoch}:20180414-%{release}
Provides:       tex(x2lcmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(x2lcmtt.fd) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-cyrillic
This bundle of macros files provides macro support (including
font encoding macros) for the use of Cyrillic characters in
fonts encoded under the T2* and X2 encodings. These encodings
cover (between them) pretty much every language that is written
in a Cyrillic alphabet.

%package -n texlive-de-macro
Provides:       tex-de-macro = %{epoch}:20180414-%{release}
Provides:       texlive-de-macro-bin = %{epoch}:20180414-%{release}
Provides:       tex-de-macro-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-de-macro-bin < 7:20170520
Provides:       tex-de-macro-doc = %{epoch}:20180414-%{release}
Provides:       texlive-de-macro-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-de-macro-doc < 7:20170520
License:        AFL
Summary:        Expand private macros in a document
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-de-macro
De-macro is a Python script that helps authors who like to use
private LaTeX macros (for example, as abbreviations). A
technical editor or a cooperating author may balk at such a
manuscript; you can avoid manuscript rejection misery by
running de-macro on it. De-macro will expand macros defined in
\(re)newcommand or \(re)newenvironment commands, within the
document, or in the document's "private" package file.

%package -n texlive-detex
Provides:       tex-detex = %{epoch}:20180414-%{release}
Provides:       texlive-detex-bin = %{epoch}:20180414-%{release}
Provides:       tex-detex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-detex-bin < 7:20170520
License:        NCSA
Summary:        Strip TeX from a source file
Requires:       texlive-base texlive-kpathsea

%description -n texlive-detex
Detex is a program to remove TeX constructs from a text file.
It recognizes the \input command. The program assumes it is
dealing with LaTeX input if it sees the string \begin{document}
in the text. In this case, it also recognizes the \include and
\includeonly commands.

%package -n texlive-diadia
Provides:       tex-diadia = %{epoch}:20180414-%{release}
Provides:       texlive-diadia-bin = %{epoch}:20180414-%{release}
Provides:       tex-diadia-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-diadia-bin < 7:20170520
Provides:       tex-diadia-doc = %{epoch}:20180414-%{release}
Provides:       texlive-diadia-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-diadia-doc < 7:20170520
License:        LPPL
Summary:        Package to keep a diabetes diary
Requires:       texlive-base texlive-kpathsea
Requires:       tex(xkeyval.sty) tex(pgfplots.sty)
Requires:       tex(pgfplotstable.sty) tex(pgfcalendar.sty)
Requires:       tex(tabularx.sty) tex(booktabs.sty)
Requires:       tex(colortbl.sty) tex(ifthen.sty)
Requires:       tex(calc.sty) tex(translations.sty)
Requires:       tex(amsmath.sty) tex(tcolorbox.sty)
Requires:       tex(environ.sty) tex(multicol.sty)
Requires:       tex(amssymb.sty)
Provides:       tex(diadia.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(diadia.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-diadia
The diadia package allows you to keep a diabetes diary.
Usually, this means keeping record of certain medical values
like blood sugar, blood pressure, pulse or weight. It might
also include other medical, pharmaceutical or nutritional data
(HbA1c, insulin doses, carbohydrate units). The diadia package
supports all of this plus more - simply by adding more columns
to the data file! It is able to evaluate the data file and
typesets formatted tables and derived plots. Furthermore, it
supports medication charts and info boxes. Supported languages:
English, German. Feel free to provide other translation files!

%package -n texlive-dosepsbin
Provides:       tex-dosepsbin = %{epoch}:20180414-%{release}
Provides:       texlive-dosepsbin-bin = %{epoch}:20180414-%{release}
Provides:       tex-dosepsbin-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dosepsbin-bin < 7:20170520
Provides:       tex-dosepsbin-doc = %{epoch}:20180414-%{release}
Provides:       texlive-dosepsbin-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dosepsbin-doc < 7:20170520
License:        GPLv2 or Artistic
Summary:        Deal with DOS binary EPS files
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-dosepsbin
A Encapsulated PostScript (EPS) file may given in a special
binary format to support the inclusion of a thumbnail. This
file format, commonly known as DOS EPS format starts with a
binary header that contains the positions of the possible
sections: Postscript (PS); Windows Metafile Format (WMF); and
Tag Image File Format (TIFF). The PS section must be present
and either the WMF file or the TIFF file should be given. The
package provides a Perl program that will extract any of the
sections of such a file, in particular providing a 'text'-form
EPS file for use with (La)TeX.

%package -n texlive-dtl
Provides:       tex-dtl = %{epoch}:20180414-%{release} texlive-dtl-bin = %{epoch}:20180414-%{release}
Provides:       tex-dtl-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dtl-bin < 7:20170520
License:        Public Domain
Summary:        Tools to dis-assemble and re-assemble DVI files
Requires:       texlive-base texlive-kpathsea

%description -n texlive-dtl
DTL (DVI Text Language) is a means of expressing the content of
a DVI file, which is readily readable by humans. The DTL bundle
contains an assembler dt2dv (which produces DVI files from DTL
files) and a disassembler dv2dt (which produces DTL files from
DVI files). The DTL bundle was developed so as to avoid some
infelicities of dvitype (among other pressing reasons).

%package -n texlive-dtxgen
Provides:       tex-dtxgen = %{epoch}:20180414-%{release}
Provides:       texlive-dtxgen-bin = %{epoch}:20180414-%{release}
Provides:       tex-dtxgen-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dtxgen-bin < 7:20170520
Provides:       tex-dtxgen-doc = %{epoch}:20180414-%{release}
Provides:       texlive-dtxgen-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dtxgen-doc < 7:20170520
License:        GPL+
Summary:        Creates a template for a self-extracting .dtx file
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-dtxgen
The bash script dtxgen creates a template for a self-extracting
.dtx file. It is useful for those who plan to create a new
Documented LaTeX Source (.dtx) file.

%package -n texlive-dvi2tty
Provides:       tex-dvi2tty = %{epoch}:20180414-%{release}
Provides:       texlive-dvi2tty-bin = %{epoch}:20180414-%{release}
Provides:       tex-dvi2tty-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dvi2tty-bin < 7:20170520
License:        GPL+
Summary:        Produce ASCII from DVI
Requires:       texlive-base texlive-kpathsea

%description -n texlive-dvi2tty
A DVI driver to produce an ASCII representation of the
document. The original version was written in Pascal, and the
present author translated the program to C.

%package -n texlive-dviasm
Provides:       tex-dviasm = %{epoch}:20180414-%{release}
Provides:       texlive-dviasm-bin = %{epoch}:20180414-%{release}
Provides:       tex-dviasm-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dviasm-bin < 7:20170520
Provides:       tex-dviasm-doc = %{epoch}:20180414-%{release}
Provides:       texlive-dviasm-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dviasm-doc < 7:20170520
License:        GPLv3+
Summary:        A utility for editing DVI files
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-dviasm
A Python script to support changing or creating DVI files via
disassembling into text, editing, and then reassembling into
binary format. It supports advanced features such as adding a
preprint number or watermarks.

%package -n texlive-dvicopy
Provides:       tex-dvicopy = %{epoch}:20180414-%{release}
Provides:       texlive-dvicopy-bin = %{epoch}:20180414-%{release}
Provides:       tex-dvicopy-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dvicopy-bin < 7:20170520
License:        GPL+
Summary:        Copy DVI files, flattening VFs
Requires:       texlive-base texlive-kpathsea

%description -n texlive-dvicopy
DVICOPY is a utility program that allows one to take a DVI file
that references composite fonts (VF) and convert it into a DVI
file that does not contain such references. It also serves as a
basis for writing DVI drivers (much like DVItype).

%package -n texlive-dvidvi
Provides:       tex-dvidvi = %{epoch}:20180414-%{release}
Provides:       texlive-dvidvi-bin = %{epoch}:20180414-%{release}
Provides:       tex-dvidvi-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dvidvi-bin < 7:20170520
License:        Copyright only
Summary:        Convert one DVI file into another
Requires:       texlive-base texlive-kpathsea

%description -n texlive-dvidvi
The output DVI file's contents are specified by page selection
commands; series of pages and page number ranges may be
specified, as well as inclusions and exclusions.

%package -n texlive-dviinfox
Provides:       tex-dviinfox = %{epoch}:20180414-%{release}
Provides:       texlive-dviinfox-bin = %{epoch}:20180414-%{release}
License:        MIT
Summary:        Perl script to print DVI meta information
BuildArch:      noarch
Requires:       texlive-base texlive-kpathsea
Requires:       perl-interpreter

%description -n texlive-dviinfox
The package provides a perl script which prints information
about a DVI file. It also supports XeTeX XDV format.

%package -n texlive-dviljk
Provides:       tex-dviljk = %{epoch}:20180414-%{release}
Provides:       texlive-dviljk-bin = %{epoch}:20180414-%{release}
Provides:       tex-dviljk-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dviljk-bin < 7:20170520
License:        GPL+
Summary:        DVI to Laserjet output
Requires:       texlive-base texlive-kpathsea

%description -n texlive-dviljk
A dvi driver for the LaserJet printers, using kpathsea
recursive file searching.

%package -n texlive-dvipdfmx
Provides:       tex-dvipdfmx = %{epoch}:20180414-%{release}
Provides:       texlive-dvipdfmx-bin = %{epoch}:20180414-%{release}
Provides:       tex-dvipdfmx-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dvipdfmx-bin < 7:20170520
Provides:       tex-dvipdfmx-doc = %{epoch}:20180414-%{release}
Provides:       texlive-dvipdfmx-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dvipdfmx-doc < 7:20170520
Provides:       dvipdfmx = %{epoch}:20180414-%{release} dvipdfm = %{epoch}:20180414-%{release}
License:        GPL+
Summary:        An extended version of dvipdfm
Requires:       texlive-base texlive-glyphlist
Requires:       texlive-kpathsea
Provides:       tex(dvipdfmx.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(cid-x.map) = %{epoch}:20180414-%{release}
Provides:       tex(ckx.map) = %{epoch}:20180414-%{release}

%description -n texlive-dvipdfmx
Dvipdfmx (formerly dvipdfm-cjk) is a development of dvipdfm
created to support multi-byte character encodings and large
character sets for East Asian languages. Dvipdfmx, if "called"
with the name dvipdfm, operates in a "dvipdfm compatibility"
mode, so that users of the both packages need only keep one
executable. A secondary design goal is to support as many "PDF"
features as does pdfTeX. There being no documentation as such,
users are advised to consult the documentation of dvipdfm (as
well, of course, as the package Readme.

%package -n texlive-dvipng
Provides:       tex-dvipng = %{epoch}:20180414-%{release}
Provides:       texlive-dvipng-bin = %{epoch}:20180414-%{release}
Provides:       tex-dvipng-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dvipng-bin < 7:20170520
Provides:       tex-dvipng-doc = %{epoch}:20180414-%{release}
Provides:       texlive-dvipng-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dvipng-doc < 7:20170520
Provides:       dvipng = %{epoch}:20180414-%{release}
License:        LGPLv2+
Summary:        A fast DVI to PNG/GIF converter
Requires:       texlive-base texlive-kpathsea

%description -n texlive-dvipng
This program makes PNG and/or GIF graphics from DVI files as
obtained from TeX and its relatives. Its benefits include:
Speed. It offers very fast rendering of DVI as bitmap files,
which makes it suitable for generating large amounts of images
on-the-fly, as needed in preview-latex, WeBWorK and others; It
does not read the postamble, so it can be started before TeX
finishes. There is a --follow switch that makes dvipng wait at
end-of-file for further output, unless it finds the POST marker
that indicates the end of the DVI; Interactive query of
options. dvipng can read options interactively through stdin,
and all options are usable. It is even possible to change the
input file through this interface. Support for PK, VF,
PostScript Type1, and TrueType fonts, colour specials, and
inclusion of PostScript, PNG, JPEG or GIF images.

%package -n texlive-dvipos
Provides:       tex-dvipos = %{epoch}:20180414-%{release}
Provides:       texlive-dvipos-bin = %{epoch}:20180414-%{release}
Provides:       tex-dvipos-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dvipos-bin < 7:20170520
License:        LPPL
Summary:        dvipos package
Requires:       texlive-base texlive-kpathsea

%description -n texlive-dvipos
dvipos package.

%package -n texlive-dvips
Provides:       tetex-dvips = %{epoch}:20180414-%{release}
Provides:       tex-dvips = %{epoch}:20180414-%{release}
Provides:       texlive-dvips-bin = %{epoch}:20180414-%{release}
Provides:       tex-dvips-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dvips-bin < 7:20170520
Provides:       tex-dvips-doc = %{epoch}:20180414-%{release}
Provides:       texlive-dvips-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dvips-doc < 7:20170520
License:        GPL+
Summary:        A DVI to PostScript driver
Requires:       texlive-base texlive-kpathsea
Provides:       tex(canonex.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(cx.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(deskjet.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(dfaxhigh.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(dvired.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(epson.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(ibmvga.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(ljfour.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(qms.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(toshiba.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(6w.enc) = %{epoch}:20180414-%{release}
Provides:       tex(7t.enc) = %{epoch}:20180414-%{release}
Provides:       tex(8a.enc) = %{epoch}:20180414-%{release}
Provides:       tex(8r.enc) = %{epoch}:20180414-%{release}
Provides:       tex(ad.enc) = %{epoch}:20180414-%{release}
Provides:       tex(ansinew.enc) = %{epoch}:20180414-%{release}
Provides:       tex(asex.enc) = %{epoch}:20180414-%{release}
Provides:       tex(asexp.enc) = %{epoch}:20180414-%{release}
Provides:       tex(dc.enc) = %{epoch}:20180414-%{release}
Provides:       tex(dvips.enc) = %{epoch}:20180414-%{release}
Provides:       tex(ec.enc) = %{epoch}:20180414-%{release}
Provides:       tex(extex.enc) = %{epoch}:20180414-%{release}
Provides:       tex(funky.enc) = %{epoch}:20180414-%{release}
Provides:       tex(odvips.enc) = %{epoch}:20180414-%{release}
Provides:       tex(q-cs-uni.enc) = %{epoch}:20180414-%{release}
Provides:       tex(q-ec-uni.enc) = %{epoch}:20180414-%{release}
Provides:       tex(q-l7x-uni.enc) = %{epoch}:20180414-%{release}
Provides:       tex(q-qx-uni.enc) = %{epoch}:20180414-%{release}
Provides:       tex(q-rm-uni.enc) = %{epoch}:20180414-%{release}
Provides:       tex(q-t2a-uni.enc) = %{epoch}:20180414-%{release}
Provides:       tex(q-t2b-uni.enc) = %{epoch}:20180414-%{release}
Provides:       tex(q-t2c-uni.enc) = %{epoch}:20180414-%{release}
Provides:       tex(q-t5-uni.enc) = %{epoch}:20180414-%{release}
Provides:       tex(q-texnansi-uni.enc) = %{epoch}:20180414-%{release}
Provides:       tex(q-ts1-uni.enc) = %{epoch}:20180414-%{release}
Provides:       tex(qx.enc) = %{epoch}:20180414-%{release}
Provides:       tex(stormex.enc) = %{epoch}:20180414-%{release}
Provides:       tex(tex256.enc) = %{epoch}:20180414-%{release}
Provides:       tex(texmext.enc) = %{epoch}:20180414-%{release}
Provides:       tex(texmital.enc) = %{epoch}:20180414-%{release}
Provides:       tex(texmsym.enc) = %{epoch}:20180414-%{release}
Provides:       tex(texnansx.enc) = %{epoch}:20180414-%{release}
Provides:       tex(blackdvi.sty) = %{epoch}:20180414-%{release}
Provides:       tex(blackdvi.tex) = %{epoch}:20180414-%{release}
Provides:       tex(colordvi.sty) = %{epoch}:20180414-%{release}
Provides:       tex(colordvi.tex) = %{epoch}:20180414-%{release}
Provides:       tex(rotate.sty) = %{epoch}:20180414-%{release}
Provides:       tex(rotate.tex) = %{epoch}:20180414-%{release}
Provides:       tex(dvips) = %{epoch}:20180414-%{release}
Requires:       texlive-latex-fonts

%description -n texlive-dvips
This package has been withdrawn from CTAN, and bundled into the
distributions' package sets. The current sources of dvips may
be found in the distribution of dvipsk which forms part of the
TeX Live sources.

%package -n texlive-dvisvgm
Provides:       tex-dvisvgm = %{epoch}:20180414-%{release}
Provides:       texlive-dvisvgm-bin = %{epoch}:20180414-%{release}
Provides:       tex-dvisvgm-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-dvisvgm-bin < 7:20170520
License:        GPL+
Summary:        Convert DVI files to Scalable Vector Graphics format (SVG)
Requires:       texlive-base texlive-kpathsea

%description -n texlive-dvisvgm
Dvisvgm is a command line utility that converts TeX DVI files
to the XML-based Scalable Vector Graphics (SVG) format. It
provides full font support including virtual fonts, font maps,
and sub-fonts. If necessary, dvisvgm vectorizes Metafont's
bitmap output in order to always create lossless scalable
output. The embedded SVG fonts can optionally be replaced with
graphics paths so that applications that don't support SVG
fonts are enabled to render the graphics properly. Besides many
other features, dvisvgm also supports color, emTeX, tpic, PDF
mapfile and PostScript specials.

%package -n texlive-ebong
Provides:       tex-ebong = %{epoch}:20180414-%{release}
Provides:       texlive-ebong-bin = %{epoch}:20180414-%{release}
Provides:       tex-ebong-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ebong-bin < 7:20170520
Provides:       tex-ebong-doc = %{epoch}:20180414-%{release}
Provides:       texlive-ebong-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ebong-doc < 7:20170520
License:        Public Domain
Summary:        Utility for writing Bengali in Rapid Roman Format
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-ebong
A tool (preprocessor) for writing your pRaa-ne-r ka-thaa in the
bengali langauage. It allows one to write the text in Rapid
Roman Bangla and convert it to the bangtex format by a python
program. All LaTeX markups are preserved in the target file.

%package -n texlive-eplain
Provides:       tex-eplain = %{epoch}:20180414-%{release}
Provides:       texlive-eplain-bin = %{epoch}:20180414-%{release}
Provides:       tex-eplain-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-eplain-bin < 7:20170520
Provides:       tex-eplain-doc = %{epoch}:20180414-%{release}
Provides:       texlive-eplain-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-eplain-doc < 7:20170520
License:        GPLv2+
Summary:        Extended plain TeX macros
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-pdftex texlive-tetex
Requires(post,postun): coreutils
Provides:       tex(arrow.tex) = %{epoch}:20180414-%{release}
Provides:       tex(btxmac.tex) = %{epoch}:20180414-%{release}
Provides:       tex(eplain.tex) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-eplain
An extended version of the plain TeX format, adding support for
bibliographies, tables of contents, enumerated lists, verbatim
input of files, numbered equations, tables, two-column output,
footnotes, hyperlinks in PDF output and commutative diagrams.
Eplain can also load some of the more useful LaTeX packages,
notably graphics, graphicx (an extended of version of
graphics), color, autopict (a package instance of the LaTeX
picture code), psfrag, and url.

%package -n texlive-epspdf
Provides:       tex-epspdf = %{epoch}:20180414-%{release}
Provides:       texlive-epspdf-bin = %{epoch}:20180414-%{release}
Provides:       tex-epspdf-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-epspdf-bin < 7:20170520
Provides:       tex-epspdf-doc = %{epoch}:20180414-%{release}
Provides:       texlive-epspdf-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-epspdf-doc < 7:20170520
License:        GPL+
Summary:        Converter for PostScript, EPS and PDF
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-epspdf
Epspdftk.tcl is a GUI ps/eps/pdf converter. Epspdf.tlu, its
command-line backend, can be used by itself. Options include
grayscaling, cropping margins and single-page selection. Some
conversion options are made possible by converting in multiple
steps.

%package -n texlive-epstopdf
Provides:       tex-epstopdf = %{epoch}:20180414-%{release}
Provides:       texlive-epstopdf-bin = %{epoch}:20180414-%{release}
Provides:       tex-epstopdf-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-epstopdf-bin < 7:20170520
Provides:       tex-epstopdf-doc = %{epoch}:20180414-%{release}
Provides:       texlive-epstopdf-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-epstopdf-doc < 7:20170520
License:        BSD
Summary:        Convert EPS to 'encapsulated' PDF using Ghostscript
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-epstopdf
Epstopdf is a Perl script that converts an EPS file to an
'encapsulated' PDF file (a single page file whose media box is
the same as the original EPS's bounding box). The resulting
file suitable for inclusion by PDFTeX as an image. The script
is adapted to run both on Windows and on Unix-alike systems.
The script makes use of Ghostscript for the actual conversion
to PDF. It assumes Ghostscript version 6.51 or later, and (by
default) suppresses its automatic rotation of pages where most
of the text is not horizontal. LaTeX users may make use of the
epstopdf package, which will run the epstopdf script "on the
fly", thus giving the illusion that PDFLaTeX is accepting EPS
graphic files.

%package -n texlive-exceltex
Provides:       tex-exceltex = %{epoch}:20180414-%{release}
Provides:       texlive-exceltex-bin = %{epoch}:20180414-%{release}
Provides:       tex-exceltex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-exceltex-bin < 7:20170520
Provides:       tex-exceltex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-exceltex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-exceltex-doc < 7:20170520
License:        GPL+
Summary:        Get data from Excel files into LaTeX
Requires:       texlive-base texlive-kpathsea
Requires:       tex(ulem.sty) tex(color.sty)
Provides:       tex(exceltex.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-exceltex
Exceltex is a LaTeX package combined with a helper program
written in Perl. It provides an easy to use yet powerfull and
flexible way to get data from Spreadsheets into LaTeX. In
contrast to other solutions, exceltex does not seek to make the
creation of tables in LaTeX easier, but to get data from
Spreadsheets into LaTeX as easily as possible. The Excel (TM)
file format only acts as an interface between the spreadsheet
application and exceltex beacause it is easily accessible (via
the Spreadsheet::ParseExcel Perl module) and because most
spreadsheet applications are able to read and write Excel
files.

%package -n texlive-fig4latex
Provides:       tex-fig4latex = %{epoch}:20180414-%{release}
Provides:       texlive-fig4latex-bin = %{epoch}:20180414-%{release}
Provides:       tex-fig4latex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-fig4latex-bin < 7:20170520
Provides:       tex-fig4latex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-fig4latex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-fig4latex-doc < 7:20170520
License:        GPLv3+
Summary:        Management of figures for large LaTeX documents
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-fig4latex
Fig4LaTeX simplifies management of the figures in a large LaTeX
document. Fig4LaTeX is appropriate for projects that include
figures with graphics created by XFig -- in particular,
graphics which use the combined PS/LaTeX (or PDF/LaTeX) export
method. An example document (with its output) is provided.

%package -n texlive-findhyph
Provides:       tex-findhyph = %{epoch}:20180414-%{release}
Provides:       texlive-findhyph-bin = %{epoch}:20180414-%{release}
Provides:       tex-findhyph-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-findhyph-bin < 7:20170520
Provides:       tex-findhyph-doc = %{epoch}:20180414-%{release}
Provides:       texlive-findhyph-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-findhyph-doc < 7:20170520
License:        GPL+
Summary:        Find hyphenated words in a document
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-findhyph
Findhyph is a Perl script that will analyse the log file from
running your document with \tracingparagraphs=1 set. The output
contains enough context to enable you to find the hyphenated
word that's being referenced.

%package -n texlive-fontinst
Provides:       tex-fontinst = %{epoch}:20180414-%{release}
Provides:       texlive-fontinst-bin = %{epoch}:20180414-%{release}
Provides:       tex-fontinst-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-fontinst-bin < 7:20170520
Provides:       tex-fontinst-doc = %{epoch}:20180414-%{release}
Provides:       texlive-fontinst-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-fontinst-doc < 7:20170520
License:        LPPL
Summary:        Help with installing fonts for TeX and LaTeX
Requires:       texlive-base texlive-kpathsea
Requires:       tex(color.sty) tex(amstext.sty)
Provides:       tex(bbox.sty) = %{epoch}:20180414-%{release}
Provides:       tex(cfntinst.sty) = %{epoch}:20180414-%{release}
Provides:       tex(fontinst.sty) = %{epoch}:20180414-%{release}
Provides:       tex(finstmsc.sty) = %{epoch}:20180414-%{release}
Provides:       tex(fontinst.sty) = %{epoch}:20180414-%{release}
Provides:       tex(multislot.sty) = %{epoch}:20180414-%{release}
Provides:       tex(xfntinst.sty) = %{epoch}:20180414-%{release}
Provides:       tex(csc2x.tex) = %{epoch}:20180414-%{release}
Provides:       tex(csckrn2x.tex) = %{epoch}:20180414-%{release}
Provides:       tex(osf2x.tex) = %{epoch}:20180414-%{release}
Provides:       tex(fontdoc.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-fontinst
TeX macros for converting Adobe Font Metric files to TeX metric
and virtual font format. Fontinst helps mainly with the number
crunching and shovelling parts of font installation. This means
in practice that it creates a number of files which give the
TeX metrics (and related information) for a font family that
(La)TeX needs to do any typesetting in these fonts. Fontinst
furthermore makes it easy to create fonts containing glyphs
from more than one base font, taking advantage of (e.g.)
"expert" font sets. Fontinst cannot examine files to see if
they contain any useful information, nor automatically search
for files or work with binary file formats; those tasks must
normally be done manually or with the help of some other tool,
such as the pltotf and vptovf programs.

%package -n texlive-fontools
Provides:       tex-fontools = %{epoch}:20180414-%{release}
Provides:       texlive-fontools-bin = %{epoch}:20180414-%{release}
Provides:       tex-fontools-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-fontools-bin < 7:20170520
Provides:       tex-fontools-doc = %{epoch}:20180414-%{release}
Provides:       texlive-fontools-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-fontools-doc < 7:20170520
License:        GPLv2+
Summary:        Tools to simplify using fonts (especially TT/OTF ones)
Requires:       texlive-base texlive-kpathsea
Provides:       tex(fontools_ly1.enc) = %{epoch}:20180414-%{release}
Provides:       tex(fontools_ot1.enc) = %{epoch}:20180414-%{release}
Provides:       tex(fontools_t1.enc) = %{epoch}:20180414-%{release}
Provides:       tex(fontools_ts1.enc) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-fontools
This package provides a few tools to ease using fonts
(especially Truetype/Opentype ones) with Latex and fontinst:
afm2afm - reencode .afm files; designed to replace fontinst's
\reencodefont for big .afm files; autoinst - simplify the use
of the LCDF TypeTools by creating a command file for otftotfm,
plus .fd and .sty files; and ot2kpx - extract all kerning pairs
from an OpenType font.

%package -n texlive-fontware
Provides:       tex-fontware = %{epoch}:20180414-%{release}
Provides:       texlive-fontware-bin = %{epoch}:20180414-%{release}
Provides:       tex-fontware-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-fontware-bin < 7:20170520
License:        LPPL
Summary:        fontware package
Requires:       texlive-base texlive-kpathsea

%description -n texlive-fontware
fontware package.

%package -n texlive-fragmaster
Provides:       tex-fragmaster = %{epoch}:20180414-%{release}
Provides:       texlive-fragmaster-bin = %{epoch}:20180414-%{release}
Provides:       tex-fragmaster-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-fragmaster-bin < 7:20170520
Provides:       tex-fragmaster-doc = %{epoch}:20180414-%{release}
Provides:       texlive-fragmaster-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-fragmaster-doc < 7:20170520
License:        GPL+
Summary:        Using psfrag with PDFLaTeX
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-fragmaster
Fragmaster enables you to use psfrag with PDFLaTeX. It takes
EPS files and psfrag substitution definition files, and
produces PDF and EPS files with the substitutions included.

%package -n texlive-getmap
Provides:       tex-getmap = %{epoch}:20180414-%{release}
Provides:       texlive-getmap-bin = %{epoch}:20180414-%{release}
Provides:       tex-getmap-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-getmap-bin < 7:20170520
Provides:       tex-getmap-doc = %{epoch}:20180414-%{release}
Provides:       texlive-getmap-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-getmap-doc < 7:20170520
License:        LPPL
Summary:        Download OpenStreetMap maps for use in documents
Requires:       texlive-base texlive-kpathsea
Requires:       tex(xkeyval.sty) tex(stringenc.sty)
Requires:       tex(ifthen.sty)
Provides:       tex(getmap.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(getmap.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-getmap
The package provides a simple interface to OpenStreetMap, and
to Google Maps "map images". In the simplest case, it is
sufficient to specify the address you need (if you don't, the
package will use its own default). The package loads the map
image using an external lua script (invoked via \write 18:
LaTeX must be running with \write 18 enabled). The ("external")
lua script may be used from the command line; a bash version is
provided.

%package -n texlive-glossaries
Provides:       tex-glossaries = %{epoch}:20180414-%{release}
Provides:       texlive-glossaries-bin = %{epoch}:20180414-%{release}
Provides:       tex-glossaries-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-glossaries-bin < 7:20170520
Provides:       tex-glossaries-doc = %{epoch}:20180414-%{release}
Provides:       texlive-glossaries-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-glossaries-doc < 7:20170520
License:        LPPL 1.3
Summary:        Create glossaries and lists of acronyms
Requires:       texlive-base texlive-kpathsea
Requires:       tex(tracklang.sty) tex(ifthen.sty)
Requires:       tex(xkeyval.sty) tex(mfirstuc.sty)
Requires:       tex(textcase.sty) tex(xfor.sty)
Requires:       tex(datatool-base.sty) tex(amsgen.sty)
Requires:       tex(etoolbox.sty) tex(glossary-super.sty)
Requires:       tex(glossary-tree.sty) tex(translator.sty)
Requires:       tex(accsupp.sty) tex(longtable.sty)
Requires:       tex(array.sty) tex(multicol.sty)
Requires:       tex(supertabular.sty)
Provides:       tex(glossaries-babel.sty) = %{epoch}:20180414-%{release}
Provides:       tex(glossaries-compatible-207.sty) = %{epoch}:20180414-%{release}
Provides:       tex(glossaries-compatible-307.sty) = %{epoch}:20180414-%{release}
Provides:       tex(glossaries-polyglossia.sty) = %{epoch}:20180414-%{release}
Provides:       tex(glossaries-prefix.sty) = %{epoch}:20180414-%{release}
Provides:       tex(glossaries.sty) = %{epoch}:20180414-%{release}
Provides:       tex(glossaries-accsupp.sty) = %{epoch}:20180414-%{release}
Provides:       tex(glossary-hypernav.sty) = %{epoch}:20180414-%{release}
Provides:       tex(glossary-inline.sty) = %{epoch}:20180414-%{release}
Provides:       tex(glossary-list.sty) = %{epoch}:20180414-%{release}
Provides:       tex(glossary-long.sty) = %{epoch}:20180414-%{release}
Provides:       tex(glossary-longragged.sty) = %{epoch}:20180414-%{release}
Provides:       tex(glossary-mcols.sty) = %{epoch}:20180414-%{release}
Provides:       tex(glossary-super.sty) = %{epoch}:20180414-%{release}
Provides:       tex(glossary-superragged.sty) = %{epoch}:20180414-%{release}
Provides:       tex(glossary-tree.sty) = %{epoch}:20180414-%{release}
Provides:       tex(example-glossaries-acronym-desc.tex) = %{epoch}:20180414-%{release}
Provides:       tex(example-glossaries-acronym.tex) = %{epoch}:20180414-%{release}
Provides:       tex(example-glossaries-acronyms-lang.tex) = %{epoch}:20180414-%{release}
Provides:       tex(example-glossaries-brief.tex) = %{epoch}:20180414-%{release}
Provides:       tex(example-glossaries-childnoname.tex) = %{epoch}:20180414-%{release}
Provides:       tex(example-glossaries-cite.tex) = %{epoch}:20180414-%{release}
Provides:       tex(example-glossaries-images.tex) = %{epoch}:20180414-%{release}
Provides:       tex(example-glossaries-long.tex) = %{epoch}:20180414-%{release}
Provides:       tex(example-glossaries-multipar.tex) = %{epoch}:20180414-%{release}
Provides:       tex(example-glossaries-parent.tex) = %{epoch}:20180414-%{release}
Provides:       tex(example-glossaries-symbols.tex) = %{epoch}:20180414-%{release}
Provides:       tex(example-glossaries-url.tex) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-glossaries
The glossaries package supports acronyms and multiple
glossaries, and has provision for operation in several
languages (using the facilities of either babel or
polyglossia). New entries are defined to have a name and
description (and optionally an associated symbol). Support for
multiple languages is offered, and plural forms of terms may be
specified. An additional package, glossaries-accsupp, can make
use of the accsupp package mechanisms for accessibility support
for PDF files containing glossaries. The user may define new
glossary styles, and preambles and postambles can be specified.
There is provision for loading a database of terms, but only
terms used in the text will be added to the relevant glossary.
The package uses an indexing program to provide the actual
glossary; either makeindex or xindy may serve this purpose, and
a Perl script is provided to serve as interface. The package
distribution also provides the mfirstuc package, for changing
the first letter of a word to upper case. The package
supersedes the author's glossary package (which is now
obsolete), and a conversion tool is provided.

%package -n texlive-glyphlist
Provides:       tex-glyphlist = %{epoch}:20180414-%{release}
License:        LPPL
Summary:        glyphlist package
BuildArch:      noarch
Requires:       texlive-base texlive-kpathsea

%description -n texlive-glyphlist
glyphlist package.

%package -n texlive-gregoriotex
Provides:       tex-gregoriotex = %{epoch}:20180414-%{release}
Provides:       texlive-gregoriotex-bin = %{epoch}:20180414-%{release}
Provides:       tex-gregoriotex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-gregoriotex-bin < 7:20170520
Provides:       tex-gregoriotex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-gregoriotex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-gregoriotex-doc < 7:20170520
License:        GPLv3
Summary:        Engraving Gregorian Chant scores
Requires:       texlive-base texlive-kpathsea
Provides:       tex(gregoriosyms.sty) = %{epoch}:20180414-%{release}
Provides:       tex(gregoriotex.sty) = %{epoch}:20180414-%{release}
Provides:       tex(gregoriotex-signs.tex) = %{epoch}:20180414-%{release}
Provides:       tex(gregoriotex-syllable.tex) = %{epoch}:20180414-%{release}
Provides:       tex(gregoriotex.tex) = %{epoch}:20180414-%{release}
Provides:       tex(gregoriotex-main.tex) = %{epoch}:20180414-%{release}
Provides:       tex(gsp-default.tex) = %{epoch}:20180414-%{release}
Provides:       tex(gregoriotex-nabc.tex) = %{epoch}:20180414-%{release}
Provides:       tex(gregoriotex-symbols.tex) = %{epoch}:20180414-%{release}
Provides:       tex(gregoriotex-chars.tex) = %{epoch}:20180414-%{release}
Provides:       tex(gregoriotex-spaces.tex) = %{epoch}:20180414-%{release}

%description -n texlive-gregoriotex
Gregorio is a software application for engraving Gregorian
Chant scores on a computer. Gregorio's main job is to convert a
gabc file (simple text representation of a score) into a
GregorioTeX file, which makes TeX able to create a PDF of your
score.

%package -n texlive-gsftopk
Provides:       tex-gsftopk = %{epoch}:20180414-%{release}
Provides:       texlive-gsftopk-bin = %{epoch}:20180414-%{release}
Provides:       tex-gsftopk-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-gsftopk-bin < 7:20170520
License:        GPL+
Summary:        Convert "ghostscript fonts" to PK files
Requires:       texlive-base texlive-kpathsea

%description -n texlive-gsftopk
Designed for use with xdvi and dvips this utility converts
Adobe Type 1 fonts to PK bitmap format. It should not
ordinarily be much used nowadays, since both its target
applications are now capable of dealing with Type 1 fonts,
direct.

%package -n texlive-installfont
Provides:       tex-installfont = %{epoch}:20180414-%{release}
Provides:       texlive-installfont-bin = %{epoch}:20180414-%{release}
Provides:       tex-installfont-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-installfont-bin < 7:20170520
Provides:       tex-installfont-doc = %{epoch}:20180414-%{release}
Provides:       texlive-installfont-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-installfont-doc < 7:20170520
License:        LPPL
Summary:        A bash script for installing a LaTeX font family
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-installfont
With this script you can install a LaTeX font family
(PostScript Type 1, TrueType and OpenType formats are
supported). Font series from light to ultra bold, and (faked)
small caps and (faked) slanted shapes are supported, but not
expert fonts. The script will rename the fonts automatically
(optional) or will otherwise expect the *.afm files and the
font files (in PostScript Type1 format) named in the Karl Berry
scheme (e.g. 5bbr8a.pfb). After running the script, you should
have a working font installation in your local TeX tree.

%package -n texlive-jadetex
Provides:       tex-jadetex = %{epoch}:20180414-%{release}
Provides:       texlive-jadetex-bin = %{epoch}:20180414-%{release}
Provides:       tex-jadetex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-jadetex-bin < 7:20170520
Provides:       tex-jadetex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-jadetex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-jadetex-doc < 7:20170520
Provides:       jadetex = %{epoch}:20180414-%{release}
License:        MIT
Summary:        Macros supporting Jade DSSSL output
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-latex texlive-passivetex
Requires:       texlive-pdftex texlive-tetex
Requires:       texlive-tex
Requires(post,postun): coreutils
Provides:       tex(dsssl.def) = %{epoch}:20180414-%{release}
Provides:       tex(uentities.sty) = %{epoch}:20180414-%{release}
Provides:       tex(ut1omlgc.fd) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-jadetex
Macro package on top of LaTeX to typeset TeX output of the Jade
DSSSL implementation.

%package -n texlive-jfmutil
Provides:       tex-jfmutil = %{epoch}:20180414-%{release}
Provides:       texlive-jfmutil-bin = %{epoch}:20180414-%{release}
License:        MIT
Summary:        Utility to process pTeX-extended TFM and VF
BuildArch:      noarch
Requires:       texlive-base texlive-kpathsea

%description -n texlive-jfmutil
This program provides functionality to process data files (JFM
and VF) that form logical fonts used in (u)pTeX. The functions
currently available include: The mutual conversion between
Japanese virtual fonts (pairs of VF and JFM) and files in the
"ZVP format", which is an original text format representing
data in virtual fonts. This function can be seen as a
counterpart to the vftovp/vptovf programs. The mutual
conversion between VF files alone and files in the "ZVP0
format", which is a subset of the ZVP format.

%package -n texlive-kotex-utils
Provides:       tex-kotex-utils = %{epoch}:20180414-%{release}
Provides:       texlive-kotex-utils-bin = %{epoch}:20180414-%{release}
Provides:       tex-kotex-utils-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-kotex-utils-bin < 7:20170520
Provides:       tex-kotex-utils-doc = %{epoch}:20180414-%{release}
Provides:       texlive-kotex-utils-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-kotex-utils-doc < 7:20170520
License:        LPPL
Summary:        Utility scripts and support files for typesetting Korean
Requires:       texlive-base texlive-kotex-utf
Requires:       texlive-kpathsea
BuildArch:      noarch

%description -n texlive-kotex-utils
The bundle provides scripts and support files for index
generation in Korean language typesetting. The files belong to
the ko.TeX bundle.

%package -n texlive-kpathsea
License:        LGPLv2+
Summary:        Path searching library for TeX-related files
Provides:       kpathsea = %{epoch}:20180414-%{release}
Obsoletes:      kpathsea < 20180414
Provides:       tex-kpathsea = %{epoch}:20180414-%{release}
Provides:       texlive-kpathsea-bin = %{epoch}:20180414-%{release}
Provides:       tex-kpathsea-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-kpathsea-bin < 7:20170520
Provides:       tex-kpathsea-doc = %{epoch}:20180414-%{release}
Provides:       texlive-kpathsea-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-kpathsea-doc < 7:20170520
Requires:       coreutils grep texlive-base texlive-tetex
Provides:       tex(fmtutil.cnf) = %{epoch}:20180414-%{release}
Provides:       tex(mktex.cnf) = %{epoch}:20180414-%{release}
Provides:       tex(texmf.cnf) = %{epoch}:20180414-%{release}

%description -n texlive-kpathsea
Kpathsea is a library and utility programs which provide path
searching facilities for TeX file types, including the self-
locating feature required for movable installations, layered on
top of a general search mechanism.

%package -n texlive-l3build
Provides:       tex-l3build = %{epoch}:20180414-%{release}
Provides:       texlive-l3build-bin = %{epoch}:20180414-%{release}
Provides:       tex-l3build-doc = %{epoch}:20180414-%{release}
Provides:       texlive-l3build-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-l3build-doc < 7:20180414
License:        LPPL
Summary:        A testing and building system for (La)TeX
Provides:       tex(regression-test.tex) = %{epoch}:20180414-%{release}
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-l3build
The build system supports testing and building LaTeX3 code, on
Linux, Mac OS X and Windows systems. The package offers: A unit
testing system for (La)TeX code (whether kernel code or
contributed packages); A system for typesetting package
documentation; and An automated process for creating CTAN
releases.

%package -n texlive-lacheck
Provides:       tex-lacheck = %{epoch}:20180414-%{release}
Provides:       texlive-lacheck-bin = %{epoch}:20180414-%{release}
Provides:       tex-lacheck-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-lacheck-bin < 7:20170520
License:        GPL+
Summary:        LaTeX checker
Requires:       texlive-base texlive-kpathsea

%description -n texlive-lacheck
Lacheck is a tool for finding common mistakes in LaTeX
documents. The distribution includes sources, and executables
for OS/2 and Win32 environments.

%package -n texlive-latex
Provides:       tex-latex = %{epoch}:20180414-%{release}
Provides:       tetex-latex = %{epoch}:20180414-%{release}
Provides:       texlive-latex-bin = %{epoch}:20180414-%{release}
Provides:       tex-latex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latex-bin < 7:20170520
Provides:       texlive-latex-bin-bin = %{epoch}:20180414-%{release}
Provides:       tex-latex-bin-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latex-bin-bin < 7:20170520
Provides:       tex-latex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-latex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latex-doc < 7:20170520
License:        LPPL 1.3
Summary:        A TeX macro package that defines LaTeX
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-luatex texlive-pdftex
Requires:       texlive-latexconfig texlive-latex-fonts
Requires:       texlive-tetex
Requires(post,postun): coreutils
Requires:       tex(multicol.sty) tex(url.sty)
Requires:       tex(hyperref.sty)
Provides:       tex(alltt.sty) = %{epoch}:20180414-%{release}
Provides:       tex(ansinew.def) = %{epoch}:20180414-%{release}
Provides:       tex(applemac.def) = %{epoch}:20180414-%{release}
Provides:       tex(article.cls) = %{epoch}:20180414-%{release}
Provides:       tex(article.sty) = %{epoch}:20180414-%{release}
Provides:       tex(ascii.def) = %{epoch}:20180414-%{release}
Provides:       tex(bezier.sty) = %{epoch}:20180414-%{release}
Provides:       tex(bk10.clo) = %{epoch}:20180414-%{release}
Provides:       tex(bk11.clo) = %{epoch}:20180414-%{release}
Provides:       tex(bk12.clo) = %{epoch}:20180414-%{release}
Provides:       tex(book.cls) = %{epoch}:20180414-%{release}
Provides:       tex(book.sty) = %{epoch}:20180414-%{release}
Provides:       tex(cp1250.def) = %{epoch}:20180414-%{release}
Provides:       tex(cp1252.def) = %{epoch}:20180414-%{release}
Provides:       tex(cp1257.def) = %{epoch}:20180414-%{release}
Provides:       tex(cp437.def) = %{epoch}:20180414-%{release}
Provides:       tex(cp437de.def) = %{epoch}:20180414-%{release}
Provides:       tex(cp850.def) = %{epoch}:20180414-%{release}
Provides:       tex(cp852.def) = %{epoch}:20180414-%{release}
Provides:       tex(cp858.def) = %{epoch}:20180414-%{release}
Provides:       tex(cp865.def) = %{epoch}:20180414-%{release}
Provides:       tex(decmulti.def) = %{epoch}:20180414-%{release}
Provides:       tex(doc.sty) = %{epoch}:20180414-%{release}
Provides:       tex(docstrip.tex) = %{epoch}:20180414-%{release}
Provides:       tex(exscale.sty) = %{epoch}:20180414-%{release}
Provides:       tex(fix-cm.sty) = %{epoch}:20180414-%{release}
Provides:       tex(fixltx2e.sty) = %{epoch}:20180414-%{release}
Provides:       tex(flafter.sty) = %{epoch}:20180414-%{release}
Provides:       tex(fleqn.clo) = %{epoch}:20180414-%{release}
Provides:       tex(fleqn.sty) = %{epoch}:20180414-%{release}
Provides:       tex(fltrace.sty) = %{epoch}:20180414-%{release}
Provides:       tex(fontenc.sty) = %{epoch}:20180414-%{release}
Provides:       tex(fontmath.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(fonttext.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(graphpap.sty) = %{epoch}:20180414-%{release}
Provides:       tex(idx.tex) = %{epoch}:20180414-%{release}
Provides:       tex(ifthen.sty) = %{epoch}:20180414-%{release}
Provides:       tex(inputenc.sty) = %{epoch}:20180414-%{release}
Provides:       tex(lablst.tex) = %{epoch}:20180414-%{release}
Provides:       tex(latex209.def) = %{epoch}:20180414-%{release}
Provides:       tex(latexbug.tex) = %{epoch}:20180414-%{release}
Provides:       tex(latexrelease.sty) = %{epoch}:20180414-%{release}
Provides:       tex(latexsym.sty) = %{epoch}:20180414-%{release}
Provides:       tex(latin1.def) = %{epoch}:20180414-%{release}
Provides:       tex(latin10.def) = %{epoch}:20180414-%{release}
Provides:       tex(latin2.def) = %{epoch}:20180414-%{release}
Provides:       tex(latin3.def) = %{epoch}:20180414-%{release}
Provides:       tex(latin4.def) = %{epoch}:20180414-%{release}
Provides:       tex(latin5.def) = %{epoch}:20180414-%{release}
Provides:       tex(latin9.def) = %{epoch}:20180414-%{release}
Provides:       tex(leqno.clo) = %{epoch}:20180414-%{release}
Provides:       tex(leqno.sty) = %{epoch}:20180414-%{release}
Provides:       tex(letter.cls) = %{epoch}:20180414-%{release}
Provides:       tex(letter.sty) = %{epoch}:20180414-%{release}
Provides:       tex(lppl.tex) = %{epoch}:20180414-%{release}
Provides:       tex(ltnews.cls) = %{epoch}:20180414-%{release}
Provides:       tex(ltxcheck.tex) = %{epoch}:20180414-%{release}
Provides:       tex(ltxdoc.cls) = %{epoch}:20180414-%{release}
Provides:       tex(ltxguide.cls) = %{epoch}:20180414-%{release}
Provides:       tex(macce.def) = %{epoch}:20180414-%{release}
Provides:       tex(makeidx.sty) = %{epoch}:20180414-%{release}
Provides:       tex(minimal.cls) = %{epoch}:20180414-%{release}
Provides:       tex(newlfont.sty) = %{epoch}:20180414-%{release}
Provides:       tex(next.def) = %{epoch}:20180414-%{release}
Provides:       tex(nfssfont.tex) = %{epoch}:20180414-%{release}
Provides:       tex(oldlfont.sty) = %{epoch}:20180414-%{release}
Provides:       tex(omlcmm.fd) = %{epoch}:20180414-%{release}
Provides:       tex(omlcmr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(omlenc.def) = %{epoch}:20180414-%{release}
Provides:       tex(omllcmm.fd) = %{epoch}:20180414-%{release}
Provides:       tex(omscmr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(omscmsy.fd) = %{epoch}:20180414-%{release}
Provides:       tex(omsenc.def) = %{epoch}:20180414-%{release}
Provides:       tex(omslcmsy.fd) = %{epoch}:20180414-%{release}
Provides:       tex(omxcmex.fd) = %{epoch}:20180414-%{release}
Provides:       tex(omxlcmex.fd) = %{epoch}:20180414-%{release}
Provides:       tex(openbib.sty) = %{epoch}:20180414-%{release}
Provides:       tex(ot1cmdh.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot1cmfib.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot1cmfr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot1cmr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot1cmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot1cmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot1cmvtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot1enc.def) = %{epoch}:20180414-%{release}
Provides:       tex(ot1lcmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot1lcmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ot4enc.def) = %{epoch}:20180414-%{release}
Provides:       tex(preload.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(proc.cls) = %{epoch}:20180414-%{release}
Provides:       tex(proc.sty) = %{epoch}:20180414-%{release}
Provides:       tex(report.cls) = %{epoch}:20180414-%{release}
Provides:       tex(report.sty) = %{epoch}:20180414-%{release}
Provides:       tex(sample2e.tex) = %{epoch}:20180414-%{release}
Provides:       tex(sfonts.def) = %{epoch}:20180414-%{release}
Provides:       tex(shortvrb.sty) = %{epoch}:20180414-%{release}
Provides:       tex(showidx.sty) = %{epoch}:20180414-%{release}
Provides:       tex(size10.clo) = %{epoch}:20180414-%{release}
Provides:       tex(size11.clo) = %{epoch}:20180414-%{release}
Provides:       tex(size12.clo) = %{epoch}:20180414-%{release}
Provides:       tex(slides.cls) = %{epoch}:20180414-%{release}
Provides:       tex(slides.def) = %{epoch}:20180414-%{release}
Provides:       tex(slides.sty) = %{epoch}:20180414-%{release}
Provides:       tex(small2e.tex) = %{epoch}:20180414-%{release}
Provides:       tex(source2e.tex) = %{epoch}:20180414-%{release}
Provides:       tex(syntonly.sty) = %{epoch}:20180414-%{release}
Provides:       tex(t1cmdh.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t1cmfib.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t1cmfr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t1cmr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t1cmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t1cmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t1cmvtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t1enc.def) = %{epoch}:20180414-%{release}
Provides:       tex(t1enc.sty) = %{epoch}:20180414-%{release}
Provides:       tex(t1lcmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(t1lcmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(testpage.tex) = %{epoch}:20180414-%{release}
Provides:       tex(texsys.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(textcomp.sty) = %{epoch}:20180414-%{release}
Provides:       tex(tracefnt.sty) = %{epoch}:20180414-%{release}
Provides:       tex(ts1cmr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ts1cmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ts1cmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ts1cmvtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ts1enc.def) = %{epoch}:20180414-%{release}
Provides:       tex(tuenc.def) = %{epoch}:20180414-%{release}
Provides:       tex(tulmdh.fd) = %{epoch}:20180414-%{release}
Provides:       tex(tulmr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(tulmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(tulmssq.fd) = %{epoch}:20180414-%{release}
Provides:       tex(tulmssq.fd) = %{epoch}:20180414-%{release}
Provides:       tex(tulmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(tulmvtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ucmr.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ucmss.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ucmtt.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ulasy.fd) = %{epoch}:20180414-%{release}
Provides:       tex(ullasy.fd) = %{epoch}:20180414-%{release}
Provides:       tex(utf8-test.tex) = %{epoch}:20180414-%{release}
Provides:       tex(utf8.def) = %{epoch}:20180414-%{release}
Provides:       tex(utf8test.tex) = %{epoch}:20180414-%{release}
Provides:       texlive-texmf-latex = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texmf-latex < 20180414
BuildArch:      noarch

%description -n texlive-latex
LaTeX is a widely-used macro package for TeX, providing many
basic document formating commands extended by a wide range of
packages. It is a development of Leslie Lamport's LaTeX 2.09,
and superseded the older system in June 1994. The basic
distribution is catalogued separately, at latex-base; apart
from a large set of contributed packages and third-party
documentation (elsewhere on the archive), the distribution
includes: - a bunch of required packages, which LaTeX authors
are "entitled to assume" will be present on any system running
LaTeX; and - a minimal set of documentation detailing
differences from the 'old' version of LaTeX in the areas of
user commands, font selection and control, class and package
writing, font encodings, configuration options and modification
of LaTeX.

%package -n texlive-latex-git-log
Provides:       tex-latex-git-log = %{epoch}:20180414-%{release}
Provides:       texlive-latex-git-log-bin = %{epoch}:20180414-%{release}
Provides:       tex-latex-git-log-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latex-git-log-bin < 7:20170520
Provides:       tex-latex-git-log-doc = %{epoch}:20180414-%{release}
Provides:       texlive-latex-git-log-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latex-git-log-doc < 7:20170520
License:        GPLv3+
Summary:        Typeset git log information
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-latex-git-log
The program is run within a git repository, and outputs the
entire version history, as a LaTeX table. That output will
typically be redirected to a file; the author recommends
typesetting in landscape orientation.

%package -n texlive-latex-papersize
Provides:       tex-latex-papersize = %{epoch}:20180414-%{release}
Provides:       texlive-latex-papersize-bin = %{epoch}:20180414-%{release}
Provides:       tex-latex-papersize-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latex-papersize-bin < 7:20170520
Provides:       tex-latex-papersize-doc = %{epoch}:20180414-%{release}
Provides:       texlive-latex-papersize-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latex-papersize-doc < 7:20170520
License:        ASL 2.0
Summary:        Calculate LaTeX settings for any font and paper size
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-latex-papersize
The package is a Python script, whose typical use is when
preparing printed material for users with low vision. The most
effective way of doing this is to print on (notional) small
paper, and then to magnify the result; the script calculates
the settings for various font and paper sizes. More details are
to be read in the script itself.

%package -n texlive-latex2man
Provides:       tex-latex2man = %{epoch}:20180414-%{release}
Provides:       texlive-latex2man-bin = %{epoch}:20180414-%{release}
Provides:       tex-latex2man-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latex2man-bin < 7:20170520
Provides:       tex-latex2man-doc = %{epoch}:20180414-%{release}
Provides:       texlive-latex2man-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latex2man-doc < 7:20170520
License:        LPPL
Summary:        Translate LaTeX-based manual pages into Unix man format
Requires:       texlive-base texlive-kpathsea
Requires:       tex(fancyheadings.sty) tex(fancyhdr.sty)
Provides:       tex(latex2man.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(latex2man.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-latex2man
A tool to translate UNIX manual pages written with LaTeX into a
man-page format understood by the Unix man(1) command.
Alternatively HTML or TexInfo code can be produced. Output of
parts of the text may be supressed using the conditional text
feature.

%package -n texlive-latex2nemeth
Provides:       tex-latex2nemeth = %{epoch}:20180414-%{release}
Provides:       texlive-latex2nemeth-bin = %{epoch}:20180414-%{release}
Provides:       tex-latex2nemeth-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latex2nemeth-bin < 7:20170520
Provides:       tex-latex2nemeth-doc = %{epoch}:20180414-%{release}
Provides:       texlive-latex2nemeth-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latex2nemeth-doc < 7:20170520
License:        GPLv3
Summary:        Convert LaTeX source to Braille with math in Nemeth
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-latex2nemeth
After many failed attempts to transcribe real math notes and
books to Braille/Nemeth in order to deal with a real situation
(blind student in Math Dept.), we decided to develop a new
program that follows a direct, from LaTeX to Braille/Nemeth,
approach. Other attempts (such as tex4ht) failed because they
all needed an extra step to go from xml to Braille, and this
step (say, with liblouis) produced incomprehensible output
(liblouis focuses in Office apps). Our main target was the
Greek language which is only Braille level 1, but English at
level 1 is supported as well. Simple pictures in PSTricks are
also supported in order to produce tactile graphics with
specialized equipment. Note that embossing will need
LibreOffice and odt2braille as this project does not deal with
embossers' drivers.

%package -n texlive-latexdiff
Provides:       tex-latexdiff = %{epoch}:20180414-%{release}
Provides:       texlive-latexdiff-bin = %{epoch}:20180414-%{release}
Provides:       tex-latexdiff-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latexdiff-bin < 7:20170520
Provides:       tex-latexdiff-doc = %{epoch}:20180414-%{release}
Provides:       texlive-latexdiff-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latexdiff-doc < 7:20170520
License:        GPLv3+
Summary:        Determine and mark up significant differences between LaTeX files
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-latexdiff
Latexdiff is a Perl script for visual mark up and revision of
significant differences between two LaTeX files. Various
options are available for visual markup using standard LaTeX
packages such as color. Changes not directly affecting visible
text, for example in formatting commands, are still marked in
the LaTeX source. A rudimentary revision facilility is provided
by another Perl script, latexrevise, which accepts or rejects
all changes. Manual editing of the difference file can be used
to override this default behaviour and accept or reject
selected changes only.

%package -n texlive-latexfileversion
Provides:       tex-latexfileversion = %{epoch}:20180414-%{release}
Provides:       texlive-latexfileversion-bin = %{epoch}:20180414-%{release}
Provides:       tex-latexfileversion-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latexfileversion-bin < 7:20170520
Provides:       tex-latexfileversion-doc = %{epoch}:20180414-%{release}
Provides:       texlive-latexfileversion-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latexfileversion-doc < 7:20170520
License:        LPPL
Summary:        Prints the version and date of a LaTeX class or style file
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-latexfileversion
This simple shell script prints the version and date of a LaTeX
class or style file. Syntax: latexfileversion <file> This
programme handles style files (extension .sty), class files
(extension .cls), and other TeX input files. The file extension
must be given.

%package -n texlive-latexindent
Provides:       tex-latexindent = %{epoch}:20180414-%{release}
Provides:       texlive-latexindent-bin = %{epoch}:20180414-%{release}
Provides:       tex-latexindent-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latexindent-bin < 7:20170520
Provides:       tex-latexindent-doc = %{epoch}:20180414-%{release}
Provides:       texlive-latexindent-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latexindent-doc < 7:20170520
License:        GPLv3+
Summary:        Indent a LaTeX document, highlighting the programming structure
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-latexindent
The Perl script processes a LaTeX file, indenting parts so as to
highlight the structure for the reader.

%package -n texlive-latexpand
Provides:       tex-latexpand = %{epoch}:20180414-%{release}
Provides:       texlive-latexpand-bin = %{epoch}:20180414-%{release}
Provides:       tex-latexpand-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latexpand-bin < 7:20170520
Provides:       tex-latexpand-doc = %{epoch}:20180414-%{release}
Provides:       texlive-latexpand-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-latexpand-doc < 7:20170520
License:        BSD
Summary:        Expand \input and \include in a LaTeX document
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-latexpand
Latexpand is a Perl script that simply replaces \input and
\include commands with the content of the file input/included.
The script does not deal with \includeonly commands.

%package -n texlive-lcdftypetools
Provides:       tex-lcdftypetools = %{epoch}:20180414-%{release}
Provides:       lcdf-typetools = %{epoch}:20180414-%{release}
Provides:       texlive-lcdftypetools-bin = %{epoch}:20180414-%{release}
Provides:       tex-lcdftypetools-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-lcdftypetools-bin < 7:20170520
License:        GPL+
Summary:        A bundle of outline font manipulation tools
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-glyphlist

%description -n texlive-lcdftypetools
This bundle of tools comprises: Cfftot1, which translates a
Compact Font Format (CFF) font, or a PostScript-flavored
OpenType font, into PostScript Type 1 format. It correctly
handles subroutines and hints; Mmafm and mmpfb, which create
instances of multiple-master fonts (mmafm and mmpfb were
previously distributed in their own package, mminstance);
Otfinfo, which reports information about OpenType fonts, such
as the features they support and the contents of their 'size'
optical size features; Otftotfm, which creates TeX font metrics
and encodings that correspond to a PostScript-flavored OpenType
font. It will interpret glyph positionings, substitutions, and
ligatures as far as it is able. You can say which OpenType
features should be activated; T1dotlessj, creates a Type 1 font
whose only character is a dotless j matching the input font's
design; T1lint, which checks a Type 1 font for correctness;
T1reencode, which replaces a font's internal encoding with one
you specify; and T1testpage, which creates a PostScript proof
for a Type 1 font.

%package -n texlive-lib
Summary:        Shared libraries for TeX-related files
Provides:       texlive-kpathsea-lib = %{epoch}:20180414-%{release}
Provides:       texlive-kpathsea-lib(%{__isa}) = 6:2016
Obsoletes:      texlive-kpathsea-lib < 2015
Provides:       bundled(lua) = 5.2.4

%description -n texlive-lib
TeX specific shared libraries.

%package -n texlive-lib-devel
Summary:        Development files for TeX specific shared libraries
Requires:       texlive-lib%{?_isa}
Provides:       texlive-kpathsea-lib-devel = %{epoch}:20180414-%{release}
Obsoletes:      texlive-kpathsea-lib-devel < 2015

%description -n texlive-lib-devel
Development files for TeX specific shared libraries.

%package -n texlive-lilyglyphs
Provides:       tex-lilyglyphs = %{epoch}:20180414-%{release}
Provides:       texlive-lilyglyphs-bin = %{epoch}:20180414-%{release}
Provides:       tex-lilyglyphs-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-lilyglyphs-bin < 7:20170520
Provides:       tex-lilyglyphs-doc = %{epoch}:20180414-%{release}
Provides:       texlive-lilyglyphs-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-lilyglyphs-doc < 7:20170520
License:        LPPL 1.3
Summary:        Access lilypond fragments and glyphs, in LaTeX
Requires:       texlive-base texlive-kpathsea
Requires:       tex(keyval.sty) tex(pgf.sty)
Requires:       tex(adjustbox.sty)
Provides:       tex(emmentaler-11.otf) = %{epoch}:20180414-%{release}
Provides:       tex(emmentaler-13.otf) = %{epoch}:20180414-%{release}
Provides:       tex(emmentaler-14.otf) = %{epoch}:20180414-%{release}
Provides:       tex(emmentaler-16.otf) = %{epoch}:20180414-%{release}
Provides:       tex(emmentaler-18.otf) = %{epoch}:20180414-%{release}
Provides:       tex(emmentaler-20.otf) = %{epoch}:20180414-%{release}
Provides:       tex(emmentaler-23.otf) = %{epoch}:20180414-%{release}
Provides:       tex(emmentaler-26.otf) = %{epoch}:20180414-%{release}
Provides:       tex(emmentaler-brace.otf) = %{epoch}:20180414-%{release}
Provides:       tex(lilyglyphs.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-lilyglyphs
The package provides the means to include arbitrary elements of
Lilypond notation, including symbols from Lilypond's Emmentaler
font, in a LaTeX document. The package uses OpenType fonts, and
as a result must be compiled with LuaLaTeX or XeLaTeX.

%package -n texlive-listbib
Provides:       tex-listbib = %{epoch}:20180414-%{release}
Provides:       texlive-listbib-bin = %{epoch}:20180414-%{release}
Provides:       tex-listbib-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-listbib-bin < 7:20170520
Provides:       tex-listbib-doc = %{epoch}:20180414-%{release}
Provides:       texlive-listbib-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-listbib-doc < 7:20170520
License:        GPL+
Summary:        Lists contents of BibTeX files
Requires:       texlive-base texlive-kpathsea
Provides:       tex(listbib.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(listbib.sty) = %{epoch}:20180414-%{release}
Provides:       tex(listbib.tex) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-listbib
Generates listings of bibliographic data bases in BibTeX format
-- for example for archival purposes. Included is a listbib.bst
which is better suited for this purpose than the standard
styles.

%package -n texlive-listings-ext
Provides:       tex-listings-ext = %{epoch}:20180414-%{release}
Provides:       texlive-listings-ext-bin = %{epoch}:20180414-%{release}
Provides:       tex-listings-ext-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-listings-ext-bin < 7:20170520
Provides:       tex-listings-ext-doc = %{epoch}:20180414-%{release}
Provides:       texlive-listings-ext-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-listings-ext-doc < 7:20170520
License:        LPPL 1.2
Summary:        Automated input of source
Requires:       texlive-base texlive-kpathsea
Requires:       tex(listings.sty) tex(xkeyval.sty)
Provides:       tex(listings-ext.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-listings-ext
The package provides a means of marking a source, so that
samples of it may be included in a document (by means of the
listings package) in a stable fashion, regardless of any change
to the source. The markup in the source text defines tags for
blocks of source. These tags are processed by a shell script to
make a steering file that is used by the package when LaTeX is
being run.

%package -n texlive-lollipop
Provides:       tex-lollipop = %{epoch}:20180414-%{release}
Provides:       texlive-lollipop-bin = %{epoch}:20180414-%{release}
Provides:       tex-lollipop-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-lollipop-bin < 7:20170520
Provides:       tex-lollipop-doc = %{epoch}:20180414-%{release}
Provides:       texlive-lollipop-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-lollipop-doc < 7:20170520
License:        GPLv3+
Summary:        TeX made easy
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-tetex texlive-tex
Requires(post,postun): coreutils
Provides:       tex(lollipop-define.tex) = %{epoch}:20180414-%{release}
Provides:       tex(lollipop-document.tex) = %{epoch}:20180414-%{release}
Provides:       tex(lollipop-float.tex) = %{epoch}:20180414-%{release}
Provides:       tex(lollipop-fontdefs.tex) = %{epoch}:20180414-%{release}
Provides:       tex(lollipop-fonts.tex) = %{epoch}:20180414-%{release}
Provides:       tex(lollipop-heading.tex) = %{epoch}:20180414-%{release}
Provides:       tex(lollipop-lists.tex) = %{epoch}:20180414-%{release}
Provides:       tex(lollipop-output.tex) = %{epoch}:20180414-%{release}
Provides:       tex(lollipop-plain.tex) = %{epoch}:20180414-%{release}
Provides:       tex(lollipop-text.tex) = %{epoch}:20180414-%{release}
Provides:       tex(lollipop-tools.tex) = %{epoch}:20180414-%{release}
Provides:       tex(lollipop.tex) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-lollipop
Lollipop is "TeX made easy" -- it is a macro package that
functions as a toolbox for writing TeX macros. Its main aim is
to make macro writing so easy that implementing a fully new
layout in TeX would become a matter of less than an hour for an
average document. The aim is that such a task could be
accomplished by someone with only a very basic training in TeX
programming. Thus, Lollipop aims to make structured text
formatting available in environments where typical users would
switch to WYSIWYG packages for the freedom that such a
mechanism offers. In addition, development of support for
Lollipop documents written in RTL languages (such as Persian)
is underway.

%package -n texlive-ltxfileinfo
Provides:       tex-ltxfileinfo = %{epoch}:20180414-%{release}
Provides:       texlive-ltxfileinfo-bin = %{epoch}:20180414-%{release}
Provides:       tex-ltxfileinfo-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ltxfileinfo-bin < 7:20170520
Provides:       tex-ltxfileinfo-doc = %{epoch}:20180414-%{release}
Provides:       texlive-ltxfileinfo-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ltxfileinfo-doc < 7:20170520
License:        GPL+
Summary:        Print version information for a LaTeX file
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-ltxfileinfo
ltxfileinfo displays version information for LaTeX files. If no
path information is given, the file is searched using
kpsewhich. As an extra, for developers, the script will (use
the --star or --color options) check the valididity of the
\Provides... statements in the files. The script uses code from
Uwe Luck's readprov.sty.

%package -n texlive-ltximg
Provides:       tex-ltximg = %{epoch}:20180414-%{release}
Provides:       texlive-ltximg-bin = %{epoch}:20180414-%{release}
Provides:       tex-ltximg-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ltximg-bin < 7:20170520
Provides:       tex-ltximg-doc = %{epoch}:20180414-%{release}
Provides:       texlive-ltximg-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ltximg-doc < 7:20170520
License:        GPLv2+
Summary:        Split LaTeX files to sanitise a conversion process
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-ltximg
The package provides a Perl script that extracts all TikZ and
PStricks environments for separate processing to produce images
(in eps, pdf, png or jpg format) for use by a converter or the
preview bundle.

%package -n texlive-lua2dox
Provides:       tex-lua2dox = %{epoch}:20180414-%{release}
Provides:       texlive-lua2dox-bin = %{epoch}:20180414-%{release}
Provides:       tex-lua2dox-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-lua2dox-bin < 7:20170520
Provides:       tex-lua2dox-doc = %{epoch}:20180414-%{release}
Provides:       texlive-lua2dox-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-lua2dox-doc < 7:20170520
License:        LPPL 1.3
Summary:        Auto-documentation of lua code
Requires:       texlive-base texlive-kpathsea
Provides:       tex(lua.def) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-lua2dox
The package extends the well-known C-like language autodoc
tool, doxygen, to read and document lua code. In use, you edit
and test your code and periodically run the autodoc tool to
update the documentation, which may be viewed via an html
browser. Autodoc tools can read the code well enough to find
function/... declarations and document them. If the code also
contains appropriatly formatted "magic comments", the tool can
use them to supplement the documentation. The package is a
first prototype of a planned TeX2DoX tool (in development),
which will process joint (La)TeX/lua documents.

%package -n texlive-luaotfload
Provides:       tex-luaotfload = %{epoch}:20180414-%{release}
Provides:       texlive-luaotfload-bin = %{epoch}:20180414-%{release}
Provides:       tex-luaotfload-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-luaotfload-bin < 7:20170520
Provides:       tex-luaotfload-doc = %{epoch}:20180414-%{release}
Provides:       texlive-luaotfload-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-luaotfload-doc < 7:20170520
License:        GPLv2+
Summary:        OpenType 'loader' for Plain TeX and LaTeX
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-lualibs texlive-lua-alt-getopt
Requires:       tex(luatexbase.sty)
Provides:       tex(luaotfload-blacklist.cnf) = %{epoch}:20180414-%{release}
Provides:       tex(luaotfload.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-luaotfload
The package adopts the TrueType/OpenType Font loader code
provided in ConTeXt, and adapts it to use in Plain TeX and
LaTeX. It works under LuaLaTeX only.

%package -n texlive-luatex
Provides:       tex-luatex = %{epoch}:20180414-%{release}
Provides:       texlive-luatex-bin = %{epoch}:20180414-%{release}
Provides:       tex-luatex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-luatex-bin < 7:20170520
Provides:       tex-luatex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-luatex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-luatex-doc < 7:20170520
License:        GPLv2+
Summary:        The LuaTeX engine
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-tetex
Requires(post,postun): coreutils
Requires:       texlive-cm texlive-etex
Requires:       texlive-hyphen-base texlive-knuth-lib
Requires:       texlive-plain texlive-tex-ini-files
Requires:       texlive-unicode-data tex(luatex.def)
Provides:       tex(luatex-unicode-letters.tex) = %{epoch}:20180414-%{release}
Provides:       tex(luatexiniconfig.tex) = %{epoch}:20180414-%{release}

%description -n texlive-luatex
LuaTeX is an extended version of pdfTeX using Lua as an
embedded scripting language. The LuaTeX project's main
objective is to provide an open and configurable variant of TeX
while at the same time offering downward compatibility. LuaTeX
uses Unicode (as UTF-8) as its default input encoding, and is
able to use modern (OpenType) fonts (for both text and
mathematics). It should be noted that LuaTeX is still under
development; its specification has been declared stable, but
absolute stability may not in practice be assumed.

%package -n texlive-lwarp
Provides:       tex-lwarp = %{epoch}:20180414-%{release}
Provides:       texlive-lwarp-bin = %{epoch}:20180414-%{release}
Provides:       tex-lwarp-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-lwarp-bin < 7:20170520
Provides:       tex-lwarp-doc = %{epoch}:20180414-%{release}
Provides:       texlive-lwarp-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-lwarp-doc < 7:20170520
License:        LPPL
Summary:        Converts LaTeX to HTML
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-lwarp
The package causes LaTeX to directly produce HTML5 output,
using external utility programs only for the final conversion
of text and images. Math may be represented by SVG files or
MathJax. Documents may be produced by LaTeX, LuaLaTeX, or
XeLaTeX. A texlua script removes the need for system utilities
such as make and gawk, and also supports xindy and latexmk.
Configuration is automatic at the first manual compile. Print
and HTML versions of each document may coexist, each with its
own set of auxiliary files. Support files are self-generated on
request. Assistance is provided for HTML import into EPUB
conversion software and word processors.

%package -n texlive-lyluatex
Summary:        Commands to include lilypond scores within a (Lua)LaTeX document
Version:        svn47584
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(lyluatex.lua) = %{epoch}:20180414-%{release}
Provides:       tex(lyluatex.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-lyluatex
This package provides macros for the inclusion of LilyPond
scores within LuaLaTeX. It calls LilyPond to compile scores,
then includes the produced files.

%package -n texlive-make4ht
Provides:       tex-make4ht = %{epoch}:20180414-%{release}
Provides:       texlive-make4ht-bin = %{epoch}:20180414-%{release}
Provides:       tex-make4ht-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-make4ht-bin < 7:20170520
Provides:       tex-make4ht-doc = %{epoch}:20180414-%{release}
Provides:       texlive-make4ht-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-make4ht-doc < 7:20170520
License:        LPPL 1.3
Summary:        A build system for tex4ht
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-make4ht
make4ht is a simple build system for tex4ht. It is both
executable, which simplifies tex4ht execution, and a library
which can be used to create customized conversion programs.

%package -n texlive-makedtx
Provides:       tex-makedtx = %{epoch}:20180414-%{release}
Provides:       texlive-makedtx-bin = %{epoch}:20180414-%{release}
Provides:       tex-makedtx-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-makedtx-bin < 7:20170520
Provides:       tex-makedtx-doc = %{epoch}:20180414-%{release}
Provides:       texlive-makedtx-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-makedtx-doc < 7:20170520
License:        LPPL
Summary:        Perl script to help generate dtx and ins files
Requires:       texlive-base texlive-kpathsea
Provides:       tex(creatdtx.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-makedtx
The makedtx bundle is provided to help LaTeX2e developers to
write the code and documentation in separate files, and then
combine them into a single .dtx file for distribution. It
automatically generates the character table, and also writes
the associated installation (.ins) script.

%package -n texlive-makeindex
Provides:       tex-makeindex = %{epoch}:20180414-%{release}
Provides:       texlive-makeindex-bin = %{epoch}:20180414-%{release}
Provides:       tex-makeindex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-makeindex-bin < 7:20170520
Provides:       tex-makeindex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-makeindex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-makeindex-doc < 7:20170520
License:        MakeIndex
Summary:        Provides sorted index from unsorted raw data
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-makeindex
Provides:       tex(idxmac.tex) = %{epoch}:20180414-%{release}

%description -n texlive-makeindex
MakeIndex is a computer program which provides a sorted index
from unsorted raw data. MakeIndex can process raw data output
by various programs, however, it is generally used with LaTeX
and troff.

%package -n texlive-match_parens
Provides:       tex-match_parens = %{epoch}:20180414-%{release}
Provides:       texlive-match_parens-bin = %{epoch}:20180414-%{release}
Provides:       tex-match_parens-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-match_parens-bin < 7:20170520
Provides:       tex-match_parens-doc = %{epoch}:20180414-%{release}
Provides:       texlive-match_parens-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-match_parens-doc < 7:20170520
License:        GPL+
Summary:        Find mismatches of parentheses, braces, (angle) brackets, in texts
Requires:       texlive-base texlive-kpathsea
Requires:       ruby
BuildArch:      noarch

%description -n texlive-match_parens
Mismatches of parentheses, braces, (angle) brackets, especially
in TeX sources which may be rich in those, may be difficult to
trace. This little script helps you by writing your text to
standard output, after adding a left margin to your text, which
will normally be almost empty, but will clearly show any
mismatches.

%package -n texlive-mathspic
Provides:       tex-mathspic = %{epoch}:20180414-%{release}
Provides:       texlive-mathspic-bin = %{epoch}:20180414-%{release}
Provides:       tex-mathspic-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mathspic-bin < 7:20170520
Provides:       tex-mathspic-doc = %{epoch}:20180414-%{release}
Provides:       texlive-mathspic-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mathspic-doc < 7:20170520
License:        LPPL
Summary:        A Perl filter program for use with PiCTeX
Requires:       texlive-base texlive-kpathsea
Requires:       tex(prepictex.tex) tex(pictexwd.tex)
Requires:       tex(postpictex.tex)
Provides:       tex(mathspic.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-mathspic
MathsPIC(Perl) is a development of the earlier MathsPIC(DOS)
program, now implemented as a Perl script, being much more
portable than the earlier program. MathsPIC parses a plain text
input file and generates a plain text output-file containing
commands for drawing a diagram. Version 1.0 produces output
containing PiCTeX and (La)TeX commands, which may then be
processed by plain TeX or LaTeX in the usual way. MathsPIC also
outputs a comprehensive log-file. MathsPIC facilitates creating
figures using PiCTeX by providing an environment for
manipulating named points and also allows the use of variables
and maths (advance, multiply, and divide)--in short--it takes
the pain out of PiCTeX.

%package -n texlive-metafont
Provides:       tex-metafont = %{epoch}:20180414-%{release}
Provides:       texlive-metafont-bin = %{epoch}:20180414-%{release}
Provides:       tex-metafont-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-metafont-bin < 7:20170520
License:        Knuth
Summary:        A system for specifying fonts
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-tetex
Requires(post,postun): coreutils
Provides:       tex(mf.mf) = %{epoch}:20180414-%{release}
Provides:       tex(plain.mf) = %{epoch}:20180414-%{release}
Provides:       tex(cmmf.ini) = %{epoch}:20180414-%{release}
Provides:       tex(mf.ini) = %{epoch}:20180414-%{release}
Provides:       tex(mode2dpi.mf) = %{epoch}:20180414-%{release}
Provides:       tex(mode2dpixy.mf) = %{epoch}:20180414-%{release}
Provides:       tex(modename.mf) = %{epoch}:20180414-%{release}
Provides:       tex(modes.mf) = %{epoch}:20180414-%{release}
Provides:       tex(ps2mfbas.mf) = %{epoch}:20180414-%{release}

%description -n texlive-metafont
The program takes a semi-algorithmic specification of a font,
and produces a bitmap font (whose properties are defined by a
set of parameters of the target device), and a set metrics for
use by TeX. The bitmap output may be converted into a format
directly usable by a device driver, etc., by the tools provided
in the parallel mfware distribution.

%package -n texlive-metapost
Provides:       tex-metapost = %{epoch}:20180414-%{release}
Provides:       texlive-metapost-bin = %{epoch}:20180414-%{release}
Provides:       tex-metapost-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-metapost-bin < 7:20170520
Provides:       tex-metapost-doc = %{epoch}:20180414-%{release}
Provides:       texlive-metapost-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-metapost-doc < 7:20170520
License:        LGPLv2+
Summary:        A development of Metafont for creating graphics
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-tetex
Provides:       tex(freeeuro.afm) = %{epoch}:20180414-%{release}
Provides:       tex(psyrgo.afm) = %{epoch}:20180414-%{release}
Provides:       tex(zpzdr-reversed.afm) = %{epoch}:20180414-%{release}
Provides:       tex(groff.enc) = %{epoch}:20180414-%{release}
Provides:       tex(troff-updmap.map) = %{epoch}:20180414-%{release}
Provides:       tex(troff.map) = %{epoch}:20180414-%{release}
Provides:       tex(freeeuro.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pagd8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pagdo8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pagk8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pagko8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pbkd8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pbkdi8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pbkl8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pbkli8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pcrb8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pcrbo8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pcrr8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pcrro8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(phvb8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(phvb8gn.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(phvbo8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(phvbo8gn.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(phvr8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(phvr8gn.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(phvro8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(phvro8gn.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pncb8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pncbi8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pncr8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pncri8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pplb8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pplbi8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pplr8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pplri8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(psyrgo.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(ptmb8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(ptmbi8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(ptmr8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(ptmri8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(pzcmi8g.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(zpzdr-reversed.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(freeeuro.pfa) = %{epoch}:20180414-%{release}
Provides:       tex(mfplain.ini) = %{epoch}:20180414-%{release}
Provides:       tex(trfonts.map) = %{epoch}:20180414-%{release}
Provides:       tex(mproof.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mpsproof.tex) = %{epoch}:20180414-%{release}

%description -n texlive-metapost
MetaPost uses a language based on that of Metafont to produce
precise technical illustrations. Its output is scalable
PostScript or SVG, rather than the bitmaps Metafont creates.

%package -n texlive-mex
Provides:       tex-mex = %{epoch}:20180414-%{release} texlive-mex-bin = %{epoch}:20180414-%{release}
Provides:       tex-mex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mex-bin < 7:20170520
Provides:       tex-mex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-mex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mex-doc < 7:20170520
License:        Public Domain
Summary:        Polish formats for TeX
Requires:       texlive-base texlive-hyphen-polish
Requires:       texlive-kpathsea texlive-pdftex
Requires:       texlive-pl texlive-tetex
Requires:       texlive-tex
Requires(post,postun): coreutils
Provides:       tex(lamex.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mex.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mex1.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mex2.tex) = %{epoch}:20180414-%{release}
Provides:       tex(mexconf.tex) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-mex
MeX is an adaptation of Plain TeX (MeX) and LaTeX209 (LaMeX)
formats to the Polish language and to Polish printing customs.
It contains a complete set of Metafont sources of Polish fonts,
hyphenation rules for the Polish language and sources of
formats.

%package -n texlive-mflua
Provides:       tex-mflua = %{epoch}:20180414-%{release}
Provides:       texlive-mflua-bin = %{epoch}:20180414-%{release}
Provides:       tex-mflua-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mflua-bin < 7:20170520
License:        GPL+
Summary:        A METAFONT compliant program with a Lua interpreter embedded
Requires:       texlive-base texlive-kpathsea

%description -n texlive-mflua
A METAFONT compliant program with a Lua interpreter embedded.

%package -n texlive-mfware
Provides:       tex-mfware = %{epoch}:20180414-%{release}
Provides:       texlive-mfware-bin = %{epoch}:20180414-%{release}
Provides:       tex-mfware-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mfware-bin < 7:20170520
License:        Knuth
Summary:        Supporting tools for use with Metafont
Requires:       texlive-base texlive-kpathsea

%description -n texlive-mfware
A collection of programs (as web source) for processing the
output of Metafont.

%package -n texlive-mf2pt1
Provides:       tex-mf2pt1 = %{epoch}:20180414-%{release}
Provides:       texlive-mf2pt1-bin = %{epoch}:20180414-%{release}
Provides:       tex-mf2pt1-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mf2pt1-bin < 7:20170520
Provides:       tex-mf2pt1-doc = %{epoch}:20180414-%{release}
Provides:       texlive-mf2pt1-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mf2pt1-doc < 7:20170520
License:        LPPL
Summary:        Produce PostScript Type 1 fonts from Metafont source
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-mf2pt1
mf2pt1 facilitates producing PostScript Type 1 fonts from a
Metafont source file. It is not, as the name may imply, an
automatic converter of arbitrary Metafont fonts to Type 1
format. mf2pt1 imposes a number of restrictions on the Metafont
input. If these restrictions are met, mf2pt1 will produce valid
Type 1 output with more accurate control points than can be
reverse-engineered by TeXtrace, mftrace, and other programs
which convert bitmaps to outline fonts.

%package -n texlive-mkgrkindex
Provides:       tex-mkgrkindex = %{epoch}:20180414-%{release}
Provides:       texlive-mkgrkindex-bin = %{epoch}:20180414-%{release}
Provides:       tex-mkgrkindex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mkgrkindex-bin < 7:20170520
Provides:       tex-mkgrkindex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-mkgrkindex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mkgrkindex-doc < 7:20170520
License:        LPPL
Summary:        Makeindex working with Greek
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-mkgrkindex
Makeindex is resolutely stuck with Latin-based alphabets, so
will not deal with Greek indexes, unaided. This package
provides a Perl script that will transmute the index of a Greek
document in such a way that makeindex will sort the entries
according to the rules of the Greek alphabet.

%package -n texlive-mkjobtexmf
Provides:       tex-mkjobtexmf = %{epoch}:20180414-%{release}
Provides:       texlive-mkjobtexmf-bin = %{epoch}:20180414-%{release}
Provides:       tex-mkjobtexmf-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mkjobtexmf-bin < 7:20170520
Provides:       tex-mkjobtexmf-doc = %{epoch}:20180414-%{release}
Provides:       texlive-mkjobtexmf-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mkjobtexmf-doc < 7:20170520
License:        GPLv2 or Artistic
Summary:        Generate a texmf tree for a particular job
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-mkjobtexmf
The package provides a Perl script, which runs a program and
tries to find the names of file used. Two methods are
available, option -recorder of (Web2C) TeX and the program
strace. Then it generates a directory with a texmf tree. It
checks the found files and tries sort them in this texmf tree.
The script may be used for archiving purposes or to speed up
later TeX runs.

%package -n texlive-mkpic
Provides:       tex-mkpic = %{epoch}:20180414-%{release}
Provides:       texlive-mkpic-bin = %{epoch}:20180414-%{release}
Provides:       tex-mkpic-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mkpic-bin < 7:20170520
Provides:       tex-mkpic-doc = %{epoch}:20180414-%{release}
Provides:       texlive-mkpic-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mkpic-doc < 7:20170520
License:        GPL+
Summary:        Perl interface to mfpic
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-mkpic
mkpic provides an easy interface for making small pictures with
mfpic. To this end you create an input file consisting of
commands, one per line, with space separated parameters (or you
modify the DATA section of the mkpic script, which is used if
you run it without an input file). For an extensive description
see the file mkpicdoc.pdf, which is part of the distribution.

%package -n texlive-mltex
Provides:       tex-mltex = %{epoch}:20180414-%{release}
Provides:       texlive-mltex-bin = %{epoch}:20180414-%{release}
Provides:       tex-mltex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mltex-bin < 7:20170520
Provides:       tex-mltex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-mltex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mltex-doc < 7:20170520
License:        Knuth
Summary:        The MLTeX system
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-latex texlive-pdftex
Requires:       texlive-tetex
Requires(post,postun): coreutils
Provides:       tex(lo1enc.def) = %{epoch}:20180414-%{release}
Provides:       tex(mlltxchg.def) = %{epoch}:20180414-%{release}
Provides:       tex(mltex.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-mltex
MLTeX is a modification of TeX version >=3.0 that allows the
hyphenation of words with accented letters using ordinary
Computer Modern (CM) fonts. The system is distributed as a TeX
change file.

%package -n texlive-mptopdf
Provides:       tex-mptopdf = %{epoch}:20180414-%{release}
Provides:       texlive-mptopdf-bin = %{epoch}:20180414-%{release}
Provides:       tex-mptopdf-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mptopdf-bin < 7:20170520
Provides:       tex-mptopdf-doc = %{epoch}:20180414-%{release}
Provides:       texlive-mptopdf-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-mptopdf-doc < 7:20170520
License:        LPPL
Summary:        mpost to PDF, native MetaPost graphics inclusion
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-tetex
Requires(post,postun): coreutils
Provides:       tex(mptopdf.tex) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-mptopdf
The mptopdf script does standalone conversion from mpost to
PDF, using the supp-* and syst-* files.  They also allow native
MetaPost graphics inclusion in LaTeX (via pdftex.def) and
ConTeXt.  They can be used independently of the rest of
ConTeXt, yet are maintained as part of it.  So in TeX Live we
pull them out to this separate package for the benefit of LaTeX
users who do not install the rest of ConTeXt.  This can be
found on CTAN in macros/pdftex/graphics.

%package -n texlive-multibibliography
Provides:       tex-multibibliography = %{epoch}:20180414-%{release}
Provides:       texlive-multibibliography-bin = %{epoch}:20180414-%{release}
Provides:       tex-multibibliography-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-multibibliography-bin < 7:20170520
Provides:       tex-multibibliography-doc = %{epoch}:20180414-%{release}
Provides:       texlive-multibibliography-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-multibibliography-doc < 7:20170520
License:        LPPL 1.3
Summary:        Multiple versions of a bibliography, with different sort orders
Requires:       texlive-base texlive-kpathsea
Provides:       tex(multibibliography.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-multibibliography
Conventional standards for bibliography styles impose a forced
choice between index and name/year citations, and corresponding
references. The package avoids this choice, by providing
alphabetic, sequenced, and even chronological orderings of
references. Inline citations, that integrate these
heterogeneous styles, are also supported (and work with other
bibliography packages).

%package -n texlive-musixtex
Provides:       tex-musixtex = %{epoch}:20180414-%{release}
Provides:       texlive-musixtex-bin = %{epoch}:20180414-%{release}
Provides:       tex-musixtex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-musixtex-bin < 7:20170520
Provides:       tex-musixtex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-musixtex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-musixtex-doc < 7:20170520
License:        GPLv2+
Summary:        Sophisticated music typesetting
Requires:       texlive-base texlive-kpathsea
Provides:       tex(musixadd.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixadf.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixbar.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixbbm.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixblx.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixbm.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixcho.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixcpt.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixcrd.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixdat.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixdbr.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixdia.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixec.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixeng.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixesf.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixevo.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixext.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixfll.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixgre.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixgui.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixhor.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixhou.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixhv.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixinv.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixlit.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixlyr.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixmad.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixper.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixplt.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixpoi.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixppff.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixps.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixref.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixslu.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixsqr.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixste.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixstf.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixstr.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixsty.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixtex.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixtmr.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixtri.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixcpt.sty) = %{epoch}:20180414-%{release}
Provides:       tex(musixcrd.sty) = %{epoch}:20180414-%{release}
Provides:       tex(musixfll.sty) = %{epoch}:20180414-%{release}
Provides:       tex(musixltx.tex) = %{epoch}:20180414-%{release}
Provides:       tex(musixtex.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-musixtex
MusiXTeX provides a set of macros, based on the earlier
MusicTeX, for typesetting music with TeX. To produce optimal
spacing, MusixTeX is a three-pass system: etex, musixflx, and
etex again. (Musixflx is a lua script that is provided in the
bundle.) The three-pass process, optionally followed by
processing for printed output, is automated by the musixtex
wrapper script. The package uses its own specialised fonts,
which must be available on the system for musixtex to run. This
version of MusixTeX builds upon work by Andreas Egler, whose
own version is no longer being developed. The MusiXTeX macros
are universally acknowledged to be challenging to use directly:
the pmx preprocessor compiles a simpler input language to
MusixTeX macros.

%package -n texlive-musixtnt
Provides:       tex-musixtnt = %{epoch}:20180414-%{release}
Provides:       texlive-musixtnt-bin = %{epoch}:20180414-%{release}
Provides:       tex-musixtnt-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-musixtnt-bin < 7:20170520
Provides:       tex-musixtnt-doc = %{epoch}:20180414-%{release}
Provides:       texlive-musixtnt-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-musixtnt-doc < 7:20170520
License:        GPLv2+
Summary:        A MusiXTeX extension library that enables transformations of the effect of notes commands
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-musixtex
Provides:       tex(musixtnt.tex) = %{epoch}:20180414-%{release}

%description -n texlive-musixtnt
The package includes an archive containing a MusiXTeX extension
library musixtnt, and documentation for a program:
msxlint. musixtnt.tex provides a macro \TransformNotes that
enables transformations of the effect of notes commands such
as \notes. In general, the effect of
\TransformNotes{input}{output} is that notes commands in the
source will expect their arguments to match the input pattern,
but the notes will be typeset according to the output pattern.
An example is extracting single-instrument parts from a multi-
instrument score. msxlint detects incorrectly formatted notes
lines in a MusiXTeX source file. This should be used before
using \TransformNotes.

%package -n texlive-m-tx
Provides:       tex-m-tx = %{epoch}:20180414-%{release} texlive-m-tx-bin = %{epoch}:20180414-%{release}
Provides:       tex-m-tx-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-m-tx-bin < 7:20170520
Provides:       tex-m-tx-doc = %{epoch}:20180414-%{release}
Provides:       texlive-m-tx-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-m-tx-doc < 7:20170520
License:        GPL+
Summary:        A preprocessor for pmx
Requires:       texlive-base texlive-kpathsea
Provides:       tex(mtx.tex) = %{epoch}:20180414-%{release}

%description -n texlive-m-tx
M-Tx is a preprocessor to pmx, which is itself a preprocessor
to musixtex, a music typesetting system. The prime motivation
to the development of M-Tx was to provide lyrics for music to
be typeset. In fact, pmx now provides a lyrics interface, but M-
Tx continues in use by those who prefer its language.

%package -n texlive-oberdiek
Provides:       tex-oberdiek = %{epoch}:20180414-%{release}
Provides:       tex-oberdiek-doc = %{epoch}:20180414-%{release}
Provides:       texlive-oberdiek-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-oberdiek-doc < 7:20170520
License:        LPPL
Summary:        A bundle of packages submitted by Heiko Oberdiek
Requires:       texlive-base texlive-kpathsea
Requires:       tex(ifluatex.sty) tex(intcalc.sty)
Requires:       tex(ifpdf.sty) tex(etexcmds.sty)
Requires:       tex(kvoptions.sty) tex(ifxetex.sty)
Requires:       tex(etex.sty) tex(color.sty)
Requires:       tex(keyval.sty) tex(soul.sty)
Requires:       tex(remreset.sty) tex(makematch.sty)
Requires:       tex(zref-lastpage.sty) tex(hyperref.sty)
Requires:       tex(fp-basic.sty) tex(fp-snap.sty)
Requires:       tex(graphics.sty) tex(amsmath.sty)
Requires:       tex(grfext.sty) tex(hypdoc.sty)
Requires:       tex(array.sty) tex(fontspec.sty)
Requires:       tex(unicode-math.sty) tex(doc.sty)
Requires:       tex(calc.sty) tex(thumbpdf.sty)
Requires:       tex(inputenc.sty) tex(listings.sty)
Requires:       tex(tikz.sty) tex(everyshi.sty)
Requires:       tex(parallel.sty) tex(parcolumns.sty)
Requires:       tex(lscape.sty) tex(index.sty)
Requires:       tex(zref-pagelayout.sty)
Provides:       tex(alphalph.sty) = %{epoch}:20180414-%{release}
Provides:       tex(atbegshi.sty) = %{epoch}:20180414-%{release}
Provides:       tex(bigintcalc.sty) = %{epoch}:20180414-%{release}
Provides:       tex(bitset.sty) = %{epoch}:20180414-%{release}
Provides:       tex(catchfile.sty) = %{epoch}:20180414-%{release}
Provides:       tex(embedfile.sty) = %{epoch}:20180414-%{release}
Provides:       tex(engord.sty) = %{epoch}:20180414-%{release}
Provides:       tex(eolgrab.sty) = %{epoch}:20180414-%{release}
Provides:       tex(etexcmds.sty) = %{epoch}:20180414-%{release}
Provides:       tex(fibnum.sty) = %{epoch}:20180414-%{release}
Provides:       tex(gettitlestring.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hobsub-generic.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hobsub-hyperref.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hobsub.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hologo.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hyphsubst.sty) = %{epoch}:20180414-%{release}
Provides:       tex(iflang.sty) = %{epoch}:20180414-%{release}
Provides:       tex(ifpdf.sty) = %{epoch}:20180414-%{release}
Provides:       tex(ifvtex.sty) = %{epoch}:20180414-%{release}
Provides:       tex(infwarerr.sty) = %{epoch}:20180414-%{release}
Provides:       tex(intcalc.sty) = %{epoch}:20180414-%{release}
Provides:       tex(kvdefinekeys.sty) = %{epoch}:20180414-%{release}
Provides:       tex(kvsetkeys.sty) = %{epoch}:20180414-%{release}
Provides:       tex(ltxcmds.sty) = %{epoch}:20180414-%{release}
Provides:       tex(luatex-loader.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pdftexcmds.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pdfescape.sty) = %{epoch}:20180414-%{release}
Provides:       tex(uniquecounter.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hobsub-hyperref.sty) = %{epoch}:20180414-%{release}
Provides:       tex(letltxmacro.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hopatch.sty) = %{epoch}:20180414-%{release}
Provides:       tex(xcolor-patch.sty) = %{epoch}:20180414-%{release}
Provides:       tex(atveryend.sty) = %{epoch}:20180414-%{release}
Provides:       tex(refcount.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hycolor.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hobsub.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hologo.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hyphsubst.sty) = %{epoch}:20180414-%{release}
Provides:       tex(iflang.sty) = %{epoch}:20180414-%{release}
Provides:       tex(ifpdf.sty) = %{epoch}:20180414-%{release}
Provides:       tex(ifvtex.sty) = %{epoch}:20180414-%{release}
Provides:       tex(infwarerr.sty) = %{epoch}:20180414-%{release}
Provides:       tex(intcalc.sty) = %{epoch}:20180414-%{release}
Provides:       tex(kvdefinekeys.sty) = %{epoch}:20180414-%{release}
Provides:       tex(kvsetkeys.sty) = %{epoch}:20180414-%{release}
Provides:       tex(ltxcmds.sty) = %{epoch}:20180414-%{release}
Provides:       tex(luatex-loader.sty) = %{epoch}:20180414-%{release}
Provides:       tex(luatex.sty) = %{epoch}:20180414-%{release}
Provides:       tex(magicnum.sty) = %{epoch}:20180414-%{release}
Provides:       tex(mleftright.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pdfcol.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pdfcrypt.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pdfescape.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pdfrender.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pdftexcmds.sty) = %{epoch}:20180414-%{release}
Provides:       tex(protecteddef.sty) = %{epoch}:20180414-%{release}
Provides:       tex(rotchiffre.sty) = %{epoch}:20180414-%{release}
Provides:       tex(se-ascii-print.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-ascii.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-clean7bit.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-cp1250.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-cp1251.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-cp1252.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-cp1257.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-cp437.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-cp850.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-cp852.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-cp855.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-cp858.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-cp865.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-cp866.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-dec-mcs.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-iso-8859-1.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-iso-8859-10.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-iso-8859-11.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-iso-8859-13.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-iso-8859-14.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-iso-8859-15.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-iso-8859-16.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-iso-8859-2.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-iso-8859-3.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-iso-8859-4.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-iso-8859-5.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-iso-8859-6.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-iso-8859-7.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-iso-8859-8.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-iso-8859-9.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-koi8-r.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-mac-centeuro.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-mac-cyrillic.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-mac-roman.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-nextstep.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-pdfdoc.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-utf16le.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-utf32be.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-utf32le.def) = %{epoch}:20180414-%{release}
Provides:       tex(se-utf8.def) = %{epoch}:20180414-%{release}
Provides:       tex(setouterhbox.sty) = %{epoch}:20180414-%{release}
Provides:       tex(soulutf8.sty) = %{epoch}:20180414-%{release}
Provides:       tex(stringenc.sty) = %{epoch}:20180414-%{release}
Provides:       tex(telprint.sty) = %{epoch}:20180414-%{release}
Provides:       tex(thepdfnumber.sty) = %{epoch}:20180414-%{release}
Provides:       tex(uniquecounter.sty) = %{epoch}:20180414-%{release}
Provides:       tex(accsupp-dvipdfm.def) = %{epoch}:20180414-%{release}
Provides:       tex(accsupp-dvips.def) = %{epoch}:20180414-%{release}
Provides:       tex(accsupp-pdftex.def) = %{epoch}:20180414-%{release}
Provides:       tex(accsupp.sty) = %{epoch}:20180414-%{release}
Provides:       tex(aliascnt.sty) = %{epoch}:20180414-%{release}
Provides:       tex(askinclude.sty) = %{epoch}:20180414-%{release}
Provides:       tex(atenddvi.sty) = %{epoch}:20180414-%{release}
Provides:       tex(atfi-dvipdfmx.def) = %{epoch}:20180414-%{release}
Provides:       tex(atfi-dvips.def) = %{epoch}:20180414-%{release}
Provides:       tex(atfi-pdftex.def) = %{epoch}:20180414-%{release}
Provides:       tex(attachfile2.sty) = %{epoch}:20180414-%{release}
Provides:       tex(atveryend.sty) = %{epoch}:20180414-%{release}
Provides:       tex(auxhook.sty) = %{epoch}:20180414-%{release}
Provides:       tex(bkm-dvipdfm.def) = %{epoch}:20180414-%{release}
Provides:       tex(bkm-dvips.def) = %{epoch}:20180414-%{release}
Provides:       tex(bkm-dvipsone.def) = %{epoch}:20180414-%{release}
Provides:       tex(bkm-pdftex.def) = %{epoch}:20180414-%{release}
Provides:       tex(bkm-textures.def) = %{epoch}:20180414-%{release}
Provides:       tex(bkm-vtex.def) = %{epoch}:20180414-%{release}
Provides:       tex(bmpsize-base.sty) = %{epoch}:20180414-%{release}
Provides:       tex(bmpsize-dvipdfm.def) = %{epoch}:20180414-%{release}
Provides:       tex(bmpsize-dvipdfmx.def) = %{epoch}:20180414-%{release}
Provides:       tex(bmpsize-dvips.def) = %{epoch}:20180414-%{release}
Provides:       tex(bmpsize-test.tex) = %{epoch}:20180414-%{release}
Provides:       tex(bmpsize.sty) = %{epoch}:20180414-%{release}
Provides:       tex(bookmark.sty) = %{epoch}:20180414-%{release}
Provides:       tex(centernot.sty) = %{epoch}:20180414-%{release}
Provides:       tex(chemarr.sty) = %{epoch}:20180414-%{release}
Provides:       tex(classlist.sty) = %{epoch}:20180414-%{release}
Provides:       tex(colonequals.sty) = %{epoch}:20180414-%{release}
Provides:       tex(dtx-attach.sty) = %{epoch}:20180414-%{release}
Provides:       tex(dvipscol.sty) = %{epoch}:20180414-%{release}
Provides:       tex(enparen.sty) = %{epoch}:20180414-%{release}
Provides:       tex(epstopdf-base.sty) = %{epoch}:20180414-%{release}
Provides:       tex(epstopdf.sty) = %{epoch}:20180414-%{release}
Provides:       tex(flags.sty) = %{epoch}:20180414-%{release}
Provides:       tex(grfext.sty) = %{epoch}:20180414-%{release}
Provides:       tex(grffile.sty) = %{epoch}:20180414-%{release}
Provides:       tex(holtxdoc.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hopatch.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hycolor.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hypbmsec.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hypcap.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hypdestopt.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hypdoc.sty) = %{epoch}:20180414-%{release}
Provides:       tex(hypgotoe.sty) = %{epoch}:20180414-%{release}
Provides:       tex(ifdraft.sty) = %{epoch}:20180414-%{release}
Provides:       tex(inputenx.sty) = %{epoch}:20180414-%{release}
Provides:       tex(ix-alias.def) = %{epoch}:20180414-%{release}
Provides:       tex(ix-math.def) = %{epoch}:20180414-%{release}
Provides:       tex(ix-name.def) = %{epoch}:20180414-%{release}
Provides:       tex(ix-slot.def) = %{epoch}:20180414-%{release}
Provides:       tex(ix-uc.def) = %{epoch}:20180414-%{release}
Provides:       tex(kvoptions-patch.sty) = %{epoch}:20180414-%{release}
Provides:       tex(kvoptions.sty) = %{epoch}:20180414-%{release}
Provides:       tex(letltxmacro.sty) = %{epoch}:20180414-%{release}
Provides:       tex(listingsutf8.sty) = %{epoch}:20180414-%{release}
Provides:       tex(luacolor.sty) = %{epoch}:20180414-%{release}
Provides:       tex(makerobust.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pagegrid.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pagesel.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pdfcolfoot.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pdfcolmk.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pdfcolparallel.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pdfcolparcolumns.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pdflscape.sty) = %{epoch}:20180414-%{release}
Provides:       tex(picture.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pmboxdraw.sty) = %{epoch}:20180414-%{release}
Provides:       tex(refcount.sty) = %{epoch}:20180414-%{release}
Provides:       tex(rerunfilecheck.sty) = %{epoch}:20180414-%{release}
Provides:       tex(resizegather.sty) = %{epoch}:20180414-%{release}
Provides:       tex(scrindex.sty) = %{epoch}:20180414-%{release}
Provides:       tex(selinput.sty) = %{epoch}:20180414-%{release}
Provides:       tex(settobox.sty) = %{epoch}:20180414-%{release}
Provides:       tex(stackrel.sty) = %{epoch}:20180414-%{release}
Provides:       tex(stampinclude.sty) = %{epoch}:20180414-%{release}
Provides:       tex(tabularht.sty) = %{epoch}:20180414-%{release}
Provides:       tex(tabularkv.sty) = %{epoch}:20180414-%{release}
Provides:       tex(transparent.sty) = %{epoch}:20180414-%{release}
Provides:       tex(twoopt.sty) = %{epoch}:20180414-%{release}
Provides:       tex(x-ascii.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-atarist.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-cp1250.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-cp1251.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-cp1252.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-cp1255.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-cp1257.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-cp437.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-cp850.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-cp852.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-cp855.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-cp858.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-cp865.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-cp866.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-dec-mcs.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-iso-8859-1.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-iso-8859-10.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-iso-8859-13.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-iso-8859-14.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-iso-8859-15.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-iso-8859-16.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-iso-8859-2.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-iso-8859-3.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-iso-8859-4.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-iso-8859-5.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-iso-8859-8.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-iso-8859-9.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-koi8-r.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-mac-centeuro.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-mac-cyrillic.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-mac-roman.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-nextstep.def) = %{epoch}:20180414-%{release}
Provides:       tex(x-verbatim.def) = %{epoch}:20180414-%{release}
Provides:       tex(xcolor-patch.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-abspage.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-abspos.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-base.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-counter.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-dotfill.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-env.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-hyperref.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-lastpage.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-marks.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-nextpage.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-pageattr.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-pagelayout.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-perpage.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-runs.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-savepos.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-thepage.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-titleref.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-totpages.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-user.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref-xr.sty) = %{epoch}:20180414-%{release}
Provides:       tex(zref.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-oberdiek
The bundle comprises packages to provide: accsupp: better
accessibility support for PDF files; aliascnt: 'alias
counters'; alphalph: multiple-alphabetic counting
(a...z,aa...zz,... -- up to the full extent of a TeX counter);
askinclude: replaces \includeonly by an interactive user
interface; atbegshi: a modern reimplementation of package
everyshi; atenddvi: provides \AtEndDvi command; attachfile2:
attach files to PDF files; atveryend: hooks the very end of a
document; auxhook: stick stuff at the start of the .aux file;
bigintcalc: expandable arithmetic operations with big integers
that can exceed TeX's number limits; bitset: defines and
implements the data type bit set, a vector of bits; bmpsize:
get bitmap size and resolution data; bookmark: alternative
bookmark (outline) organization for package hyperref;
catchfile: collects the contents of a file and puts it in a
macro; centernot: a horizontally-centred \not symbol; chemarr:
extensible chemists' reaction arrows; classlist: record
information about document class(es) used; colonequals: poor
man's mathematical relation symbols; dvipscol: dvips colour
stack management; embedfile: embed files in PDF documents;
engord: define counter-printing operations producing English
ordinals; eolgrab: collect arguments delimited by end of line;
epstopdf: conversion to epstopdf on the fly; etexcmds: adds a
prefix to eTeX's commands, to avoid conflicts with existing
macros; flags: setting and clearing flags in bit fields and
converting the bit field into a decimal number; gettitlestring:
clean up the string containing the title of a section, etc.;
grfext: macros for adding and reordering the list of graphics
file extensions recognised by the graphics package; grffile:
extend file name processing in the graphics bundle; hosub:
build collections of packages; holtxdoc: extra documentation
macros; hologo: bookmark-enabled logos; hopatch: safely apply
package patches; hycolor: implements the color option stuff
that is used by packages hyperref and bookmark; hypbmsec:
bookmarks in sectioning commands; hypcap: anjusting anchors of
captions; hypdestopt: optimising hyperref's pdftex driver
destinations; hypdoc: hyper-references in the LaTeX standard
doc package; hypgotoe: experimental package for links to
embedded files; hyphsubst: substitute hyphenation patterns;
ifdraft: switch for option draft; iflang: provides expandable
checks for the current language; ifluatex: looks for LuaTeX
regardless of its mode and provides the switch \ifluatex;
ifpdf: provides the \ifpdf switch; ifvtex: provides the \ifvtex
switch; infwarerr: provides a complete set of macros for
informations, warnings and error messages with support for
plain TeX; inputenx: enhanced handling of input encoding;
intcalc: provides expandable arithmetic operations with
integers; kvdefinekeys: define key-value keys in the same
manner as keyval; kvoptions: use package options in key value
format ; kvsetkeys: a variant of the \setkeys command;
letltxmacro: Let assignment for LaTeX macros; listingsutf8:
(partially) extends the listings package to UTF-8 encoding;
ltxcmds: exports some utility macros from the LaTeX kernel into
a separate namespace and also provides them for other formats
such as plain-TeX; luacolor: implements colour support based on
LuaTeX's node attributes; luatex: utilises new and extended
features and resources that LuaTeX provides; magicnum: allows
to access magic numbers by a hierarchical name system;
makerobust: make a command robust; pagegrid: prints a page grid
in the background; pagesel: select pages of a document for
output; pdfcolfoot: using pdftex's color stack for footnotes;
pdfcol: macros for setting and maintaining new color stacks;
pdfcolmk: PDFTeX COLour MarK -- fake a PDFTeX colour stack
using marks (not needed for PDFTeX 1.40.0 and later);
pdfcolparallel: fixes colour problems in package parallel;
pdfcolparcolumns: fixes colour problems in package parcolumns;
pdfcrypt: setting PDF encryption; pdfescape: pdfTeX's escape
features using TeX or e-TeX; pdflscape: landscape pages in PDF;
pdfrender: control PDF rendering modes; pdftexcmds: provide
PDFTeX primitives missing in LuaTeX; picture: dimens for
picture macros; pmboxdraw: poor man's box drawing characters;
protecteddef: define a command that protected against
expansion; refcount: using the numeric values of references;
rerunfilecheck: checksum based rerun checks on auxiliary files;
resizegather: automatically resize overly large equations;
rotchiffre: performs simple rotation cyphers; scrindex:
redefines environment 'theindex' of package 'index', if a class
from KOMA-Script is loaded; selinput: select the input encoding
by specifying pairs of input characters and their glyph names;
setouterhbox: set \hbox in outer horizontal mode; settobox:
getting box sizes; soulutf8: extends package soul and adds some
support for UTF-8; stackrel: extensions of the \stackrel
command; stampinclude: selects the files for \include by
inspecting the timestamp of the .aux file(s); stringenc:
provides \StringEncodingConvert for converting a string between
different encodings; tabularht: tabulars with height
specification; tabularkv: key value interface for tabular
parameters; telprint: print German telephone numbers;
thepdfnumber: canonical numbers for use in PDF files and
elsewhere; transparent: using a color stack for transparency
with pdftex; twoopt: commands with two optional arguments;
uniquecounter: provides unlimited unique counter; zref: a
proposed new reference system. Each of the packages is
represented by two files, a .dtx (documented source) and a PDF
file; the .ins file necessary for installation is extracted by
running the .dtx file with Plain TeX.

%package -n texlive-omegaware
Provides:       tex-omegaware = %{epoch}:20180414-%{release}
Provides:       texlive-omegaware-bin = %{epoch}:20180414-%{release}
Provides:       tex-omegaware-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-omegaware-bin < 7:20170520
Provides:       tex-omegaware-doc = %{epoch}:20180414-%{release}
Provides:       texlive-omegaware-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-omegaware-doc < 7:20170520
License:        LPPL
Summary:        Omegaware package
Requires:       texlive-base texlive-kpathsea

%description -n texlive-omegaware
Omegaware package.

%package -n texlive-patgen
Provides:       tex-patgen = %{epoch}:20180414-%{release}
Provides:       texlive-patgen-bin = %{epoch}:20180414-%{release}
Provides:       tex-patgen-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-patgen-bin < 7:20170520
License:        Knuth
Summary:        Generate hyphenation patterns
Requires:       texlive-base texlive-kpathsea

%description -n texlive-patgen
This is the last version of the program distributed by Knuth;
it advertises itself as a pattern generator for "the algorithm
used in TeX", but, of course, the patterns used in modern
distributions are Unicode-based.

%package -n texlive-pax
Provides:       tex-pax = %{epoch}:20180414-%{release} texlive-pax-bin = %{epoch}:20180414-%{release}
Provides:       tex-pax-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pax-bin < 7:20170520
Provides:       tex-pax-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pax-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pax-doc < 7:20170520
License:        GPLv2+
Summary:        Extract and reinsert PDF annotations with pdfTeX
Requires:       texlive-base texlive-kpathsea
Requires:       tex(ifpdf.sty) tex(graphicx.sty)
Requires:       tex(ltxcmds.sty) tex(kvsetkeys.sty)
Requires:       tex(kvoptions.sty) tex(auxhook.sty)
Requires:       tex(etexcmds.sty)
Provides:       tex(pax.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-pax
If PDF files are included using pdfTeX, PDF annotations are
stripped. The pax project offers a solution without altering
pdfTeX. A Java program (pax.jar) parses the PDF file that will
later be included. The program then writes the data of the
annotations into a file that can be read by TeX. The LaTeX
package pax extends the graphics package to support the scheme:
if a PDF file is included, the package looks for the file with
the annotation data, reads them and puts the annotations in the
right place.

%package -n texlive-pdfbook2
Provides:       tex-pdfbook2 = %{epoch}:20180414-%{release}
Provides:       texlive-pdfbook2-bin = %{epoch}:20180414-%{release}
Provides:       tex-pdfbook2-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pdfbook2-bin < 7:20170520
Provides:       tex-pdfbook2-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pdfbook2-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pdfbook2-doc < 7:20170520
License:        GPLv3+
Summary:        Create booklets from PDF files
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-pdfcrop texlive-pdfjam
BuildArch:      noarch

%description -n texlive-pdfbook2
This python program creates print-ready PDF files from some
input PDF files for booklet printing. The resulting files need
to be printed in landscape/long edge double sided printing. The
default paper format depends on the locale and is chosen by
pdfjam. It can be chosen using the --paper option. Before the
pdf is composed, the input file is cropped to the relevant area
in order to discard unnecessary white spaces. In this process,
all pages are cropped to the same dimensions. Extra margins can
be defined at the edges of the booklet and in the middle where
the binding occurs. The output is written to INPUT-book.pdf.
Existing files will be overwritten. All input files are
processed seperately.

%package -n texlive-pdfcrop
Provides:       tex-pdfcrop = %{epoch}:20180414-%{release}
Provides:       texlive-pdfcrop-bin = %{epoch}:20180414-%{release}
Provides:       tex-pdfcrop-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pdfcrop-bin < 7:20170520
Provides:       tex-pdfcrop-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pdfcrop-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pdfcrop-doc < 7:20170520
License:        LPPL
Summary:        Crop PDF graphics
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-pdfcrop
A Perl script that can either trim pages of any whitespace
border, or trim them of a fixed border.

%package -n texlive-pdfjam
Provides:       tex-pdfjam = %{epoch}:20180414-%{release}
Provides:       texlive-pdfjam-bin = %{epoch}:20180414-%{release}
Provides:       tex-pdfjam-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pdfjam-bin < 7:20170520
Provides:       tex-pdfjam-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pdfjam-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pdfjam-doc < 7:20170520
License:        GPLv2+
Summary:        Shell scripts interfacing to pdfpages
Requires:       texlive-base texlive-collection-latex
Requires:       texlive-kpathsea texlive-latex
Requires:       tex(pdfpages.sty)
BuildArch:      noarch

%description -n texlive-pdfjam
This is a collection of shell scripts which provide an
interface to the pdfpages LaTeX package. They do such jobs as
selecting pages, concatenating files, doing n-up formatting,
and so on.

%package -n texlive-pdflatexpicscale
Provides:       tex-pdflatexpicscale = %{epoch}:20180414-%{release}
Provides:       texlive-pdflatexpicscale-bin = %{epoch}:20180414-%{release}
Provides:       tex-pdflatexpicscale-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pdflatexpicscale-bin < 7:20170520
Provides:       tex-pdflatexpicscale-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pdflatexpicscale-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pdflatexpicscale-doc < 7:20170520
License:        LPPL
Summary:        Support software for downscaling graphics to be included by pdfLaTeX
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-pdflatexpicscale
The package provides a script to scale pictures down to a
target resolution before creating a PDF document with pdfLaTeX.

%package -n texlive-pdftex
Provides:       tex-pdftex = %{epoch}:20180414-%{release}
Provides:       texlive-pdftex-bin = %{epoch}:20180414-%{release}
Provides:       tex-pdftex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pdftex-bin < 7:20170520
Provides:       tex-pdftex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pdftex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pdftex-doc < 7:20170520
License:        GPL+
Summary:        A TeX extension for direct creation of PDF
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-tetex
Requires(post,postun): coreutils
Requires:       tex-graphics-def texlive-cm
Requires:       texlive-etex texlive-hyphen-base
Requires:       texlive-knuth-lib texlive-plain
Requires:       tex-tex-ini-files
Provides:       tex(dummy-space.map) = %{epoch}:20180414-%{release}
Provides:       tex(dummy-space.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dummy-space.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(pdftex-dvi.tex) = %{epoch}:20180414-%{release}
Provides:       tex(glyphtounicode.tex) = %{epoch}:20180414-%{release}
Provides:       tex(pdfcolor.tex) = %{epoch}:20180414-%{release}

%description -n texlive-pdftex
An extension of TeX which can be configured to directly
generate PDF documents instead of DVI. All current free TeX
distributions including TeX live, MacTeX and MiKTeX include
pdfTeX (Plain TeX) and pdfLaTeX (LaTeX). ConTeXt was designed
around use of pdfTeX (though it is now migrating towards
LuaTeX).

%package -n texlive-pdftools
Provides:       tex-pdftools = %{epoch}:20180414-%{release}
Provides:       texlive-pdftools = %{epoch}:20180414-%{release}
Provides:       tex-pdftools-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pdftools-bin < 7:20170520
License:        Public Domain
Summary:        PDF-related utilities, including PostScript-to-PDF conversion
Requires:       texlive-base texlive-kpathsea

%description -n texlive-pdftools
The command-line programs pdfopen and pdfclose allow you to
control the X Window System version of Adobe's Acrobat Reader
from the command line or from within a (shell) script. The
programs work with Acrobat Reader 5, 7, 8 and 9 for Linux, xpdf
and evince. This version derives from one written by Fabrice
Popineau for Microsoft operating systems.

%package -n texlive-pdfxup
Provides:       tex-pdfxup = %{epoch}:20180414-%{release}
Provides:       texlive-pdfxup-bin = %{epoch}:20180414-%{release}
Provides:       tex-pdfxup-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pdfxup-bin < 7:20170520
Provides:       tex-pdfxup-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pdfxup-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pdfxup-doc < 7:20170520
License:        LPPL
Summary:        Create n-up PDF pages with minimal margins
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-pdfxup
pdfxup is a unix/linux shell script that creates a PDF document
where each page is obtained by combining several pages of a PDF
file given as output.

%package -n texlive-pedigree-perl
Provides:       tex-pedigree-perl = %{epoch}:20180414-%{release}
Provides:       texlive-pedigree-perl-bin = %{epoch}:20180414-%{release}
Provides:       tex-pedigree-perl-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pedigree-perl-bin < 7:20170520
Provides:       tex-pedigree-perl-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pedigree-perl-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pedigree-perl-doc < 7:20170520
License:        GPLv2+
Summary:        Generate TeX pedigree files from CSV files
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-pedigree-perl
This program generates TeX commands to typeset pedigrees --
either TeX fragments or full LaTeX files, to be processed by
the authors' pst-pdgr package. The program has support for
multilanguage pedigrees (at the present moment the English and
Russian languages are supported).

%package -n texlive-perltex
Provides:       tex-perltex = %{epoch}:20180414-%{release}
Provides:       texlive-perltex-bin = %{epoch}:20180414-%{release}
Provides:       tex-perltex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-perltex-bin < 7:20170520
Provides:       tex-perltex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-perltex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-perltex-doc < 7:20170520
License:        LPPL
Summary:        Define LaTeX macros in terms of Perl code
Requires:       texlive-base texlive-kpathsea
Provides:       tex(perltex.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-perltex
PerlTeX is a combination Perl script (perltex.pl) and LaTeX2e
package (perltex.sty) that, together, give the user the ability
to define LaTeX macros in terms of Perl code. Once defined, a
Perl macro becomes indistinguishable from any other LaTeX
macro. PerlTeX thereby combines LaTeX's typesetting power with
Perl's programmability. PerlTeX will make use of persistent
named pipes, and thereby run more efficiently, on operating
systems that offer them (mostly Unix-like systems). Also
provided is a switch to generate a PerlTeX-free, document-
specific, noperltex.sty that is useful when distributing a
document to places where PerlTeX is not available.

%package -n texlive-petri-nets
Provides:       tex-petri-nets = %{epoch}:20180414-%{release}
Provides:       texlive-petri-nets-bin = %{epoch}:20180414-%{release}
Provides:       tex-petri-nets-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-petri-nets-bin < 7:20170520
Provides:       tex-petri-nets-doc = %{epoch}:20180414-%{release}
Provides:       texlive-petri-nets-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-petri-nets-doc < 7:20170520
License:        GPL+
Summary:        A set of TeX/LaTeX packages for drawing Petri nets
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pndraw.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pndraw.tex) = %{epoch}:20180414-%{release}
Provides:       tex(pnets.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pnets.tex) = %{epoch}:20180414-%{release}
Provides:       tex(pntext.sty) = %{epoch}:20180414-%{release}
Provides:       tex(pntext.tex) = %{epoch}:20180414-%{release}
Provides:       tex(pnversion.tex) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-petri-nets
Petri-nets offers a set of TeX/LaTeX packages about Petri nets
and related models. Three packages are available: the first
allows the user to draw Petri-nets in PostScript documents; the
second defines macros related to PBC, M-nets and B(PN) models;
and a third that combines the other two.

%package -n texlive-pfarrei
Provides:       tex-pfarrei = %{epoch}:20180414-%{release}
Provides:       texlive-pfarrei-bin = %{epoch}:20180414-%{release}
Provides:       tex-pfarrei-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pfarrei-bin < 7:20170520
Provides:       tex-pfarrei-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pfarrei-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pfarrei-doc < 7:20170520
License:        LPPL 1.3
Summary:        LaTeX support of pastors' and priests' work
Requires:       texlive-base texlive-kpathsea
Requires:       tex(ifpdf.sty) tex(pdfpages.sty)
Requires:       tex(keyval.sty)
Provides:       tex(a5toa4.tex) = %{epoch}:20180414-%{release}
Provides:       tex(pfarrei.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-pfarrei
In "Die TeXnische Komodie" (issue 1/2013) Christian Justen
described his use of LaTeX in his work as priest (similar
requirements may be encountered in the work of pastors and
other ministers of religion). One point was to arrange A5 pages
onto A4 landscape paper, either side-by-side or as a booklet.
Justen made two bash scripts for this job; the package provides
one texlua script for both requirements.

%package -n texlive-pkfix
Provides:       tex-pkfix = %{epoch}:20180414-%{release}
Provides:       tex-pkfix-bin = %{epoch}:20180414-%{release}
Provides:       texlive-pkfix-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pkfix-bin < 7:20170520
Provides:       tex-pkfix-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pkfix-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pkfix-doc < 7:20170520
License:        LPPL 1.3
Summary:        Replace pk fonts in PostScript with Type 1 fonts
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-pkfix
The perl script pkfix looks for DVIPSBitmapFont comments in
PostScript files, generated by 'not too old' dvips, and
replaces them by type 1 versions of the fonts, if possible.

%package -n texlive-pkfix-helper
Provides:       tex-pkfix-helper = %{epoch}:20180414-%{release}
Provides:       tex-pkfix-helper-bin = %{epoch}:20180414-%{release}
Provides:       texlive-pkfix-helper-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pkfix-helper-bin < 7:20170520
Provides:       tex-pkfix-helper-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pkfix-helper-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pkfix-helper-doc < 7:20170520
License:        LPPL
Summary:        Make PostScript files accessible to pkfix
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-pkfix-helper
Pkfix is a useful utility for replacing resolution-dependent
bitmapped fonts in a dvips-produced PostScript file with the
corresponding resolution-independent vector fonts.
Unfortunately, pkfix needs to parse certain PostScript comments
that appear only in files produced by dvips versions later than
5.58 (ca. 1996); it fails to work on PostScript files produced
by older versions of dvips. Pkfix-helper is a program that
attempts to insert newer-dvips comments into an older-dvips
PostScript file, thereby making the file suitable for
processing by pkfix. pkfix-helper can sometimes process
documents fully autonomously but does require the user to
verify and, if needed, correct its decisions.

%package -n texlive-pmx
Provides:       tex-pmx = %{epoch}:20180414-%{release} tex-pmx-bin = %{epoch}:20180414-%{release}
Provides:       texlive-pmx-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pmx-bin < 7:20170520
Provides:       tex-pmx-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pmx-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pmx-doc < 7:20170520
License:        GPLv2+
Summary:        Preprocessor for MusiXTeX
Requires:       texlive-base texlive-kpathsea
Provides:       tex(pmx.tex) = %{epoch}:20180414-%{release}

%description -n texlive-pmx
PMX is a preprocessor for MusiXTeX. It builds the TeX input
file from a file in a much simpler language, making most of the
layout decisions by itself. An auxiliary program makes single-
player parts from a multi-player score. For proof-listening,
PMX can make a MIDI file of your score. The present version
requires at least version 1.15 of MusiXTeX, running on an e-tex-
enhanced TeX system.

%package -n texlive-pmxchords
Provides:       tex-pmxchords = %{epoch}:20180414-%{release}
Provides:       tex-pmxchords-bin = %{epoch}:20180414-%{release}
Provides:       texlive-pmxchords-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pmxchords-bin < 7:20170520
Provides:       tex-pmxchords-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pmxchords-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pmxchords-doc < 7:20170520
License:        GPLv2+
Summary:        Produce chord information to go with pmx output
Requires:       texlive-base texlive-kpathsea
Provides:       tex(chords.tex) = %{epoch}:20180414-%{release}
Provides:       tex(chordsCZ.tex) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-pmxchords
The bundle supplements pmx, providing the means of typesetting
chords above the notes of a score. The bundle contains: macros
for typing the chords; a Lua script to transpose chord macros
to the required key signature; and support scripts for common
requirements.

%package -n texlive-pstools
Provides:       tex-pstools = %{epoch}:20180414-%{release}
Provides:       tex-pstools-bin = %{epoch}:20180414-%{release}
Provides:       texlive-pstools-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pstools-bin < 7:20170520
Provides:       tex-pstools-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pstools-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pstools-doc < 7:20170520
License:        GPL+
Summary:        Produce Encapsulated PostScript from PostScript
Requires:       texlive-base texlive-kpathsea

%description -n texlive-pstools
Produce Encapsulated PostScript Files (EPS/EPSF) from a one-
page PostScript document, or any PostScript document. A correct
Bounding Box is calculated for the EPS files and some
PostScript command sequences that can produce errorneous
results on printers are filtered. The input is cropped to
include just the image contained in the PostScript file. The
EPS files can then be included into TeX documents. Other
programs like ps2epsi (a script distributed with ghostscript)
don't always calculate the correct bounding box (because the
values are put on the PostScript stack which may get corrupted
by bad PostScript code) or they round it off, resulting in
clipping the image. Therefore ps2eps uses a resolution of 144
dpi to get the correct bounding box. Included in the
distribution is the bbox program, an application to produce
Bounding Box values for rawppm or rawpbm format files.

%package -n texlive-pst2pdf
Provides:       tex-pst2pdf = %{epoch}:20180414-%{release}
Provides:       tex-pst2pdf-bin = %{epoch}:20180414-%{release}
Provides:       texlive-pst2pdf-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pst2pdf-bin < 7:20170520
Provides:       tex-pst2pdf-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pst2pdf-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pst2pdf-doc < 7:20170520
License:        GPLv2+
Summary:        A script to compile pstricks documents via pdftex
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-pst2pdf
The script extracts the preamble of the document and runs all
\begin{postscript}...\end{postscript}
\begin{pspicture}...\end{pspicture} and
\pspicture...\endpspicture separately through LaTeX with the
same preamble as the original document; thus it creates EPS,
PNG and PDF files of these snippets. In a final PDFLaTeX run
the script replaces the environments with \includegraphics to
include the processed snippets.

%package -n texlive-pst-pdf
Provides:       tex-pst-pdf = %{epoch}:20180414-%{release}
Provides:       tex-pst-pdf-bin = %{epoch}:20180414-%{release}
Provides:       texlive-pst-pdf-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pst-pdf-bin < 7:20170520
Provides:       tex-pst-pdf-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pst-pdf-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pst-pdf-doc < 7:20170520
License:        LPPL
Summary:        Make PDF versions of graphics by processing between runs
Requires:       texlive-base texlive-kpathsea
Requires:       tex(graphicx.sty) tex(pstricks.sty)
Requires:       tex(environ.sty)
Provides:       tex(pst-pdf.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-pst-pdf
The package pst-pdf simplifies the use of graphics from
PSTricks and other PostScript code in PDF documents. As in
building a bibliography with BibTEX, additional external
programmes are invoked. In this case they are used to create a
PDF file (\PDFcontainer) that will contain all the graphics
material. In the final document these contents will be inserted
instead of the original PostScript code. The package works with
pstricks and requires a recent version of the preview package.

%package -n texlive-ps2pk
Provides:       tex-ps2pk = %{epoch}:20180414-%{release}
Provides:       tex-ps2pk-bin = %{epoch}:20180414-%{release}
Provides:       texlive-ps2pk-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ps2pk-bin < 7:20170520
Provides:       texlive-ps2pkm = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ps2pkm < 7:20170520
Provides:       texlive-ps2pkm-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ps2pkm-bin < 7:20170520
License:        MIT
Summary:        Generate a PK font from an Adobe Type 1 font
Requires:       texlive-base texlive-kpathsea

%description -n texlive-ps2pk
Generates a PK file from an Adobe Type 1 font. PK fonts are (or
used to be) valuable in enabling previewers to view documents
generated that use Type 1 fonts. The program makes use of code
donated to the X consortium by IBM.

%package -n texlive-ptex
Provides:       tex-ptex = %{epoch}:20180414-%{release} tex-ptex-bin = %{epoch}:20180414-%{release}
Provides:       texlive-ptex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ptex-bin < 7:20170520
Provides:       tex-ptex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-ptex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ptex-doc < 7:20170520
Provides:       texlive-platex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-platex-bin < 7:20170520
License:        BSD
Summary:        A TeX system for publishing in Japanese
Requires:       texlive-adobemapping texlive-base
Requires:       texlive-hyph-utf8 texlive-ipaex
Requires:       texlive-japanese texlive-japanese-otf
Requires:       texlive-kpathsea texlive-latex
Requires:       texlive-ptex-base texlive-ptex-fonts
Requires:       texlive-tetex texlive-tex
Requires:       tex(oldlfont.sty) tex(shortvrb.sty)
Requires(post,postun): coreutils
Provides:       tex(morisawa.map) = %{epoch}:20180414-%{release}

%description -n texlive-ptex
PTeX adds features related to vertical writing, and deals with
other problems in typesetting Japanese. A set of additions to a
TEXMF tree, for use with PTeX, may be found in package PTeX-
texmf. PTeX is distributed as WEB change files.

%package -n texlive-ptex-fontmaps
Provides:       tex-ptex-fontmaps = %{epoch}:20180414-%{release}
Provides:       tex-ptex-fontmaps = %{epoch}:20180414-%{release}
Provides:       texlive-ptex-fontmaps-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ptex-fontmaps-bin < 7:20170520
Provides:       tex-ptex-fontmaps-doc = %{epoch}:20180414-%{release}
Provides:       texlive-ptex-fontmaps-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ptex-fontmaps-doc < 7:20170520
Provides:       tex-jfontmaps = %{epoch}:20180414-%{release}
Provides:       texlive-jfontmaps = %{epoch}:20180414-%{release}
Obsoletes:      texlive-jfontmaps <= 6:svn40613
Provides:       tex-jfontmaps-bin = %{epoch}:20180414-%{release}
Provides:       texlive-jfontmaps-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-jfontmaps-bin <= 6:svn29848.0
Provides:       tex-jfontmaps-doc = %{epoch}:20180414-%{release}
Provides:       texlive-jfontmaps-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-jfontmaps-doc <= 6:svn40613
License:        GPLv3
Summary:        Font maps and configuration tools for Japanese/Chinese/Korean fonts with (u)ptex
Requires:       texlive-arphic-ttf texlive-baekmuk
Requires:       texlive-base texlive-ipaex
Requires:       texlive-kpathsea
BuildArch:      noarch

%description -n texlive-ptex-fontmaps
This package provides font maps and setup tools for Japanese,
Korean, Traditional Chinese, and Simplified Chinese. It is the
successor of the jfontmaps package. The files in this package
contain font maps for dvipdfmx to make various
Japanese/Chinese/Korean fonts available for (u)ptex and related
programs and formats.

%package -n texlive-ptex2pdf
Provides:       tex-ptex2pdf = %{epoch}:20180414-%{release}
Provides:       tex-ptex2pdf-bin = %{epoch}:20180414-%{release}
Provides:       texlive-ptex2pdf-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ptex2pdf-bin < 7:20170520
Provides:       tex-ptex2pdf-doc = %{epoch}:20180414-%{release}
Provides:       texlive-ptex2pdf-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ptex2pdf-doc < 7:20170520
License:        GPLv2+
Summary:        Convert Japanese TeX documents to PDF
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-ptex2pdf
The Lua script provides system-independent support of Japanese
typesetting engines in TeXworks. As TeXworks typesetting setup
does not allow for multistep processing, this script runs one
of the ptex-based programs (ptex, uptex, eptex, platex,
uplatex) followed by dvipdfmx.

%package -n texlive-purifyeps
Provides:       tex-purifyeps = %{epoch}:20180414-%{release}
Provides:       tex-purifyeps-bin = %{epoch}:20180414-%{release}
Provides:       texlive-purifyeps-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-purifyeps-bin < 7:20170520
Provides:       tex-purifyeps-doc = %{epoch}:20180414-%{release}
Provides:       texlive-purifyeps-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-purifyeps-doc < 7:20170520
License:        LPPL
Summary:        Make EPS work with both LaTeX/dvips and pdfLaTeX
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-purifyeps
While pdfLaTeX has a number of nice features, its primary
shortcoming relative to standard LaTeX+dvips is that it is
unable to read ordinary Encapsulated PostScript (EPS) files,
the most common graphics format in the LaTeX world. Purifyeps
converts EPS files into a 'purified' form that can be read by
both LaTeX+dvips and pdfLaTeX. The trick is that the standard
LaTeX2e graphics packages can parse MetaPost-produced EPS
directly. Hence, purifyeps need only convert an arbitrary EPS
file into the same stylized format that MetaPost outputs.

%package -n texlive-pygmentex
Provides:       tex-pygmentex = %{epoch}:20180414-%{release}
Provides:       tex-pygmentex-bin = %{epoch}:20180414-%{release}
Provides:       texlive-pygmentex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pygmentex-bin < 7:20170520
Provides:       tex-pygmentex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pygmentex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pythontex-doc < 7:20170520
License:        LPPL 1.3
Summary:        Use Pygments to format code listings in documents
Requires:       texlive-base texlive-kpathsea
Requires:       tex(fancyvrb.sty) tex(color.sty)
Requires:       tex(ifthen.sty) tex(caption.sty)
Requires:       tex(pgfkeys.sty) tex(efbox.sty)
Requires:       tex(mdframed.sty) tex(fvextra.sty)
Provides:       tex(pygmentex.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-pygmentex
PygmenTeX is a Python-based LaTeX package that can be used for
typesetting code listings in a LaTeX document using Pygments.
Pygments is a generic syntax highlighter for general use in all
kinds of software such as forum systems, wikis or other
applications that need to prettify source code.

%package -n texlive-pythontex
Provides:       tex-pythontex = %{epoch}:20180414-%{release}
Provides:       tex-pythontex-bin = %{epoch}:20180414-%{release}
Provides:       texlive-pythontex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pythontex-bin < 7:20170520
Provides:       tex-pythontex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-pythontex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-pythontex-doc < 7:20170520
License:        LPPL 1.3
Summary:        Run Python from within a document, typesetting the results
Requires:       texlive-base texlive-kpathsea
Requires:       tex(fancyvrb.sty) tex(etex.sty)
Requires:       tex(etoolbox.sty) tex(xstring.sty)
Requires:       tex(pgfopts.sty) tex(newfloat.sty)
Requires:       tex(currfile.sty) tex(xcolor.sty)
Requires:       tex(upquote.sty)
Provides:       tex(pythontex.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-pythontex
The package allows you to enter Python code within a LaTeX
document, execute the code, and access its output in the
original document. Python code is only executed when it has
been modified, or when it meets user-specified criteria. Code
may be divided into user-defined sessions, which automatically
run in parallel. Errors and warnings are synchronized with the
LaTeX document, so that they refer to the document's line
numbers. External dependencies can be tracked, so that code is
re-executed when the data it depends on is modified. PythonTeX
also provides syntax highlighting for code in LaTeX documents
via the Pygments syntax highlighter. The package provides a
depythontex utility, that creates a copy of the document in
which all Python code has been replaced by its output. This is
useful for journal submissions, sharing documents, and
conversion to other formats.

%package -n texlive-rubik
Provides:       tex-rubik = %{epoch}:20180414-%{release}
Provides:       tex-rubik-bin = %{epoch}:20180414-%{release}
Provides:       texlive-rubik-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-rubik-bin < 7:20170520
Provides:       tex-rubik-doc = %{epoch}:20180414-%{release}
Provides:       texlive-rubik-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-rubik-doc < 7:20170520
License:        LPPL 1.3
Summary:        Document Rubik cube configurations and rotation sequences
Requires:       texlive-base texlive-kpathsea
Requires:       tex(tikz.sty) tex(fancyvrb.sty)
Provides:       tex(rubikcube.sty) = %{epoch}:20180414-%{release}
Provides:       tex(rubikrotation.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-rubik
The bundle provides two packages: rubikcube provides commands
for typesetting Rubik cubes and their transformations; and
rubikrotation which can process a sequence of Rubik rotation
moves, with the help of a Perl package executed via \write18
(shell escape) commands.

%package -n texlive-seetexk
Provides:       tex-seetexk = %{epoch}:20180414-%{release}
Provides:       tex-seetexk-bin = %{epoch}:20180414-%{release}
Provides:       texlive-seetexk-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-seetexk-bin < 7:20170520
License:        MIT
Summary:        Utilities for manipulating DVI files
Requires:       texlive-base texlive-kpathsea

%description -n texlive-seetexk
The collection comprises: dvibook, which will rearrange the
pages of a DVI file into 'signatures' as used when printing a
book; dviconcat, for concatenating pages of DVI file(s);
dviselect, which will select pages from one DVI file to create
a new DVI file; dvitodvi, which will rearrange the pages of a
DVI file to create a new file; and libtex, a library for
manipulating the files, from the old SeeTeX project. The
utilities are provided as C source with Imakefiles, and an MS-
DOS version of dvibook is also provided.

%package -n texlive-splitindex
Provides:       tex-splitindex = %{epoch}:20180414-%{release}
Provides:       tex-splitindex-bin = %{epoch}:20180414-%{release}
Provides:       texlive-splitindex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-splitindex-bin < 7:20170520
Provides:       tex-splitindex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-splitindex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-splitindex-doc < 7:20170520
License:        LPPL
Summary:        Unlimited number of indexes
Requires:       texlive-base texlive-kpathsea
Provides:       tex(splitindex.tex) = %{epoch}:20180414-%{release}
Provides:       tex(splitidx.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-splitindex
SplitIndex consists of a LaTeX package, splitidx, and a small
program, splitindex. The package may be used to produce one
index or several indexes. Without splitindex (for example,
using the index package), the number of indexes is limited by
the number of TeX's output streams. But using the program you
may use even more than 16 indexes: splitidx outputs only a
single file \jobname.idx and the program splits that file into
several raw index files and calls your favorite index processor
for each of the files.

%package -n texlive-srcredact
Provides:       tex-srcredact = %{epoch}:20180414-%{release}
Provides:       tex-srcredact-bin = %{epoch}:20180414-%{release}
Provides:       texlive-srcredact-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-srcredact-bin < 7:20170520
Provides:       tex-srcredact-doc = %{epoch}:20180414-%{release}
Provides:       texlive-srcredact-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-srcredact-doc < 7:20170520
License:        GPLv2+
Summary:        A tool for redacting sources
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-srcredact
This package provides a tool to keep a master source,
consisting of different "chunks" intended for different
audiences. The tool allows to extract the versions intended for
different audiences and to incorporate the changes made in any
of these versions into the master document. This work was
commissioned by the Consumer Financial Protection Bureau,
United States Treasury.

%package -n texlive-sty2dtx
Provides:       tex-sty2dtx = %{epoch}:20180414-%{release}
Provides:       tex-sty2dtx-bin = %{epoch}:20180414-%{release}
Provides:       texlive-sty2dtx-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-sty2dtx-bin < 7:20170520
Provides:       tex-sty2dtx-doc = %{epoch}:20180414-%{release}
Provides:       texlive-sty2dtx-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-sty2dtx-doc < 7:20170520
License:        GPLv3+
Summary:        Create a .dtx file from a .sty file
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-sty2dtx
The package provides a Perl script that converts a .sty file
(LaTeX package) to .dtx format (documented LaTeX source), by
surrounding macro definitions with macro and macrocode
environments. The macro name is automatically inserted as an
argument to the macro environemnt. Code lines outside macro
definitions are wrapped only in macrocode environments. Empty
lines are removed. The script should not be thought to be fool
proof and 100% accurate but rather as a good start to the
business of making a .dtx file from an undocumented style file.
Full .dtx files are generated. A template based on the skeleton
file from 'dtxtut' is used. User level macros are added
automatically to the 'Usage' section of the .dtx file. A
corresponding .ins file can be generated as well.

%package -n texlive-svn-multi
Provides:       tex-svn-multi = %{epoch}:20180414-%{release}
Provides:       tex-svn-multi-bin = %{epoch}:20180414-%{release}
Provides:       texlive-svn-multi-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-svn-multi-bin < 7:20170520
Provides:       tex-svn-multi-doc = %{epoch}:20180414-%{release}
Provides:       texlive-svn-multi-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-svn-multi-doc < 7:20170520
License:        LPPL
Summary:        Subversion keywords in multi-file LaTeX documents
Requires:       texlive-base texlive-kpathsea
Requires:       tex(kvoptions.sty) tex(filehook.sty)
Requires:       tex(currfile.sty) tex(graphics.sty)
Requires:       tex(pgf.sty)
Provides:       tex(svn-multi.sty) = %{epoch}:20180414-%{release}
Provides:       tex(svnkw.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-svn-multi
This package lets you typeset keywords of the version control
system Subversion inside your LaTeX files anywhere you like.
Unlike the otherwise similar package svn the use of multiple
files for one LaTeX document is well supported. The package
uses the author's filehook and currfile packages. The package
interacts with an external Perl script, to retrieve information
necessary for the required output.

%package -n texlive-synctex
Provides:       tex-synctex = %{epoch}:20180414-%{release}
Provides:       tex-synctex-bin = %{epoch}:20180414-%{release}
Provides:       texlive-synctex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-synctex-bin < 7:20170520
License:        LPPL
Summary:        synctex package
Requires:       texlive-base texlive-kpathsea

%description -n texlive-synctex
synctex package.

%package -n texlive-tetex
License:        GPL+ and GPLv2+ and LPPL
Summary:        scripts and files originally written for or included in teTeX
Provides:       tex-tetex = %{epoch}:20180414-%{release}
Provides:       tex-tetex-bin = %{epoch}:20180414-%{release}
Provides:       texlive-tetex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-tetex-bin < 7:20170520
Provides:       tex-tetex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-tetex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-tetex-doc < 7:20170520
Requires:       texlive-base texlive-kpathsea-bin
Requires:       texlive-texlive.infra
Provides:       tex(09fbbfac.enc) = %{epoch}:20180414-%{release}
Provides:       tex(0ef0afca.enc) = %{epoch}:20180414-%{release}
Provides:       tex(10037936.enc) = %{epoch}:20180414-%{release}
Provides:       tex(1b6d048e.enc) = %{epoch}:20180414-%{release}
Provides:       tex(71414f53.enc) = %{epoch}:20180414-%{release}
Provides:       tex(74afc74c.enc) = %{epoch}:20180414-%{release}
Provides:       tex(aae443f0.enc) = %{epoch}:20180414-%{release}
Provides:       tex(b6a4d7c7.enc) = %{epoch}:20180414-%{release}
Provides:       tex(bbad153f.enc) = %{epoch}:20180414-%{release}
Provides:       tex(d9b29452.enc) = %{epoch}:20180414-%{release}
Provides:       tex(f7b6d320.enc) = %{epoch}:20180414-%{release}
Provides:       tex(mtex.enc) = %{epoch}:20180414-%{release}
Provides:       tex(base14flags.tex) = %{epoch}:20180414-%{release}
Provides:       tex(dvipdfm35.map) = %{epoch}:20180414-%{release}
Provides:       tex(dvips35.map) = %{epoch}:20180414-%{release}
Provides:       tex(mathpple.map) = %{epoch}:20180414-%{release}
Provides:       tex(pdftex35.map) = %{epoch}:20180414-%{release}
Provides:       tex(ps2pk35.map) = %{epoch}:20180414-%{release}
Provides:       tex(updmap.cfg) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-tetex
teTeX was a comprehensive distribution of TeX, LaTeX and
family, designed for ease of compilation, installation and
customisation. In 2006, Thomas Esser announced he would no
longer be able to support, or to produce new versions of,
teTeX. With the appearance of TeX live 2007 (whose Unix-system
TeX support originally derived from teTeX), no-one should be
using teTeX at all, in new applications. One of the "schemes"
available when installing TeX live provides a configuration
very close to that of the old teTeX, but using modern versions
of programs and packages.

%package -n texlive-tex
Provides:       tex-tex = %{epoch}:20180414-%{release} tex-tex-bin = %{epoch}:20180414-%{release}
Provides:       texlive-tex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-tex-bin < 7:20170520
License:        Knuth
Summary:        A sophisticated typesetting engine
Requires:       texlive-base texlive-cm
Requires:       texlive-hyphen-base texlive-knuth-lib
Requires:       texlive-kpathsea texlive-plain
Requires:       texlive-tetex
Requires(post,postun): coreutils

%description -n texlive-tex
TeX is a typesetting system that incorporates a macro
processor. A TeX source document specifies or incorporates a
number of macro definitions that instruct the TeX engine how to
typeset the document. The TeX engine also uses font metrics
generated by Metafont, or by any of several other mechanisms
that incorporate fonts from other sources into an environment
suitable for TeX. TeX has been, and continues, a basis and an
inspiration for several other programs, including e-TeX and
PDFTeX.

%package -n texlive-tex4ebook
Provides:       tex-tex4ebook = %{epoch}:20180414-%{release}
Provides:       tex-tex4ebook-bin = %{epoch}:20180414-%{release}
Provides:       texlive-tex4ebook-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-tex4ebook-bin < 7:20170520
Provides:       tex-tex4ebook-doc = %{epoch}:20180414-%{release}
Provides:       texlive-tex4ebook-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-tex4ebook-doc < 7:20170520
License:        LPPL 1.3
Summary:        Convertor from LaTeX to ebook formats
Requires:       texlive-base texlive-kpathsea
Requires:       tex(etoolbox.sty) tex(kvoptions.sty)
Requires:       tex(graphicx.sty)
Provides:       tex(tex4ebook.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-tex4ebook
This is a bundle of lua scripts and LaTeX packages for
conversion of LaTeX files to ebook formats such as epub, mobi
and epub3. tex4ht is used as conversion engine.

%package -n texlive-tex4ht
Provides:       tex-tex4ht = %{epoch}:20180414-%{release}
Provides:       tex-tex4ht-bin = %{epoch}:20180414-%{release}
Provides:       texlive-tex4ht-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-tex4ht-bin < 7:20170520
Provides:       tex-tex4ht-doc = %{epoch}:20180414-%{release}
Provides:       texlive-tex4ht-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-tex4ht-doc < 7:20170520
License:        LPPL
Summary:        Convert (La)TeX to HTML/XML
Requires:       texlive-base texlive-kpathsea
Provides:       tex(m-tex4ht.tex) = %{epoch}:20180414-%{release}
Provides:       tex(tex4ht.sty) = %{epoch}:20180414-%{release}

%description -n texlive-tex4ht
A converter from TeX and LaTeX to SGML-based formats such as
(X)HTML, MathML, OpenDocument, and DocBook, providing a
configurable (La)TeX-based authoring system for hypertext.
Tex4ht does not parse (La)TeX source (so that it avoids the
difficulties encountered by many other converters, arising from
the irregularity of (La)TeX syntax). Instead, Tex4ht uses
(La)TeX itself (with an extra macro package) to produce a non-
standard DVI file that it can then process. This technique
allows TeX4ht to approach the robustness characteristic of
restricted-syntax systems such as hyperlatex and gellmu.

%package -n texlive-texconfig
Provides:       tex-texconfig = %{epoch}:20180414-%{release}
Provides:       tex-texconfig-bin = %{epoch}:20180414-%{release}
Provides:       texlive-texconfig-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texconfig-bin < 7:20170520
License:        LPPL
Summary:        Tool to configure teTeX or TeX Live
Requires:       texlive-base texlive-kpathsea
Provides:       tex(tcfmgr.map) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-texconfig
texconfig allows one to configure and maintain TeX in an easy
and convenient manner, offering a series of dialog boxes to
the user. The directory in which texconfig is found is also
preferentially used to find subprograms.

%package -n texlive-texcount
Provides:       tex-texcount = %{epoch}:20180414-%{release}
Provides:       tex-texcount-bin = %{epoch}:20180414-%{release}
Provides:       texlive-texcount-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texcount-bin < 7:20170520
Provides:       tex-texcount-doc = %{epoch}:20180414-%{release}
Provides:       texlive-texcount-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texcount-doc < 7:20170520
License:        LPPL
Summary:        Count words in a LaTeX document
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-texcount
TeXcount is a Perl script that counts words in the text of
LaTeX files. It has rules for handling most of the common
macros, and can provide colour-coded output showing which parts
of the text have been counted. The package script is available
as a Web service via its home page.

%package -n texlive-texdef
Provides:       tex-texdef = %{epoch}:20180414-%{release}
Provides:       tex-texdef-bin = %{epoch}:20180414-%{release}
Provides:       texlive-texdef-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texdef-bin < 7:20170520
Provides:       tex-texdef-doc = %{epoch}:20180414-%{release}
Provides:       texlive-texdef-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texdef-doc < 7:20170520
License:        GPLv3+
Summary:        Display the definitions of TeX commands
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-texdef
The (Perl) script displays the definition of (La)TeX command
sequences/macros. Various options allow the selection of the
used class and package files and other things which can have
influence on the definition (before/after the preamble, inside
an environment, ...). The script creates a temporary TeX file
which is then compiled using (La)TeX to find the '\meaning' of
the command sequence. The result is formatted and presented to
the user. Length or number command sequences (dimensions,
\char..., count registers, ...) are recognized and the
contained value is also shown (using \the). Special definitions
like protected macros are also recognized and the underlying
macros are shown as well. The script will show plain TeX
definitions by default. LaTeX and ConTeXt are supported,
including flavours (pdf(la)tex, lua(la)tex, xe(la)tex, ...).
The flavour can be selected using an command line option or
over the script name: latexdef will use LaTeX as default, etc.

%package -n texlive-texdiff
Provides:       tex-texdiff = %{epoch}:20180414-%{release}
Provides:       tex-texdiff-bin = %{epoch}:20180414-%{release}
Provides:       texlive-texdiff-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texdiff-bin < 7:20170520
Provides:       tex-texdiff-doc = %{epoch}:20180414-%{release}
Provides:       texlive-texdiff-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texdiff-doc < 7:20170520
License:        GPL+ or Artistic
Summary:        Compares two (La)TeX documents to create a merged version showing changes
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-texdiff
Texdiff compares two (La)TeX documents to create a merged version showing
changes, similar to that of 'Change Tracking' in some word processors.

%package -n texlive-texdirflatten
Provides:       tex-texdirflatten = %{epoch}:20180414-%{release}
Provides:       tex-texdirflatten-bin = %{epoch}:20180414-%{release}
Provides:       texlive-texdirflatten-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texdirflatten-bin < 7:20170520
License:        GPL+ or Artistic
Summary:        Collect files related to a LaTeX job in a single directory
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-texdirflatten
The Perl script parses a LaTeX file recursively, scanning all
child files, and collects details of any included and other
data files. These component files, are then all put into a
single directory (thus "flattening" the document's directory
tree).

%package -n texlive-texdoc
Provides:       tex-texdoc = %{epoch}:20180414-%{release}
Provides:       tex-texdoc-bin = %{epoch}:20180414-%{release}
Provides:       texlive-texdoc-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texdoc-bin < 7:20170520
Provides:       tex-texdoc-doc = %{epoch}:20180414-%{release}
Provides:       texlive-texdoc-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texdoc-doc < 7:20170520
License:        GPL+
Summary:        Documentation access for TeX distributions
Requires:       texlive-base texlive-kpathsea
Provides:       tex(texdoc.cnf) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-texdoc
TeXdoc is an application for easy access to the package
documentation of a TeX distributions (i.e., .dvi, .pdf or .ps
files on the $TEXDOCS tree). It is distributed with TeX-Live
and a derivative is distributed with miktex.

%package -n texlive-texdoctk
Provides:       tex-texdoctk = %{epoch}:20180414-%{release}
Provides:       tex-texdoctk-bin = %{epoch}:20180414-%{release}
Provides:       tex-texdoctk-doc = %{epoch}:20180414-%{release}
Provides:       texlive-texdoctk-bin = %{epoch}:20180414-%{release}
Provides:       texlive-texdoctk-doc = %{epoch}:20180414-%{release}
License:        GPL+
Summary:        Easy access to package documentation
Requires:       texlive-base texlive-kpathsea
Provides:       tex(texdoctk.dat) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-texdoctk
A Perl/Tk-based GUI for easy access to package documentation
for TeX on Unix platforms; the databases it uses are based on
the texmf/doc subtrees of teTeX, but database files for local
configurations with modified/extended directories can be
derived from them. Note that texdoctk is not a viewer itself,
but an interface for finding documentation files and opening
them with the appropriate viewer; so it relies on appropriate
programs to be installed on the system. However, the choice of
these programs can be configured by the sysadmin or user. Now
only distributed as part of TeX Live, which includes a Windows
executable.

%package -n texlive-texfot
Provides:       tex-texfot = %{epoch}:20180414-%{release}
Provides:       tex-texfot-bin = %{epoch}:20180414-%{release}
Provides:       texlive-texfot-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texfot-bin < 7:20170520
Provides:       tex-texfot-doc = %{epoch}:20180414-%{release}
Provides:       texlive-texfot-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texfot-doc < 7:20170520
License:        Public Domain
Summary:        Filter clutter from the output of a TeX run
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-texfot
The package provides a small Perl script to filter the online
output from a TeX run, attempting to show only those messages
which probably deserve some change in the source. The TeX
invocation itself need not change.

%package -n texlive-texliveonfly
Provides:       tex-texliveonfly = %{epoch}:20180414-%{release}
Provides:       tex-texliveonfly-bin = %{epoch}:20180414-%{release}
Provides:       texlive-texliveonfly-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texliveonfly-bin < 7:20170520
Provides:       tex-texliveonfly-doc = %{epoch}:20180414-%{release}
Provides:       texlive-texliveonfly-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texliveonfly-doc < 7:20170520
License:        GPLv3+
Summary:        On-the-fly download of missing TeX live packages
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-texliveonfly
The package provides a script that performs 'on the fly'
downloads of missing packages, while a document is being
compiled. (This feature is already available in the MikTeX
distribution for Windows machines.) To use the script, replace
your (LaTeX) compilation command with texliveonfly.py file.tex
(default options are --engine=lualatex and --arguments="-
synctex=1 -interaction=nonstopmode", which may all be changed).
The script is designed to work on Linux distributions.

%package -n texlive-texlive-en
Provides:       tex-texlive-en = %{epoch}:20180414-%{release}
Provides:       tex-texlive-en-doc = %{epoch}:20180414-%{release}
Provides:       texlive-texlive-en-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texlive-en-doc < 7:20170520
License:        LPPL
Summary:        TeX Live manual (English)
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-texlive-en
TeX Live manual (English).

%package -n texlive-texlive-scripts
Provides:       tex-texlive-scripts = %{epoch}:20180414-%{release}
Provides:       texlive-texlive-scripts-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texlive-scripts-bin < 7:20170520
License:        LPPL
Summary:        TeX Live infrastructure programs
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-texlive.infra
BuildArch:      noarch

%description -n texlive-texlive-scripts
Includes install-tl, tl-portable, rungs, etc.; not needed for
tlmgr to run but still ours.  Not included in tlcritical.

%package -n texlive-texlive.infra
Provides:       tex-texlive.infra = %{epoch}:20180414-%{release}
Provides:       tex-texlive.infra-bin = %{epoch}:20180414-%{release}
Provides:       texlive-texlive.infra-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texlive.infra-bin < 7:20170520
Provides:       tex-texlive.infra-doc = %{epoch}:20180414-%{release}
Provides:       texlive-texlive.infra-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texlive.infra-doc < 7:20170520
License:        LPPL
Summary:        Basic TeX Live infrastructure
Requires:       texlive-base texlive-kpathsea
Provides:       tex(fmtutil-hdr.cnf) = %{epoch}:20180414-%{release}
Provides:       tex(updmap-hdr.cfg) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-texlive.infra
This package contains the files needed to get the TeX Live
tools (notably tlmgr) running: perl modules, xz binaries, plus
(sometimes) tar and wget.  These files end up in the standalone
install packages, and in the tlcritical repository.

%package -n texlive-texloganalyser
Provides:       tex-texloganalyser = %{epoch}:20180414-%{release}
Provides:       tex-texloganalyser-bin = %{epoch}:20180414-%{release}
Provides:       texlive-texloganalyser-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texloganalyser-bin < 7:20170520
Provides:       tex-texloganalyser-doc = %{epoch}:20180414-%{release}
Provides:       texlive-texloganalyser-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texloganalyser-doc < 7:20170520
License:        BSD
Summary:        Analyse TeX logs
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-texloganalyser
The perl script allows the user to extract (and display)
elements of the log file.

%package -n texlive-texosquery
Provides:       tex-texosquery = %{epoch}:20180414-%{release}
Provides:       tex-texosquery-bin = %{epoch}:20180414-%{release}
Provides:       texlive-texosquery-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texosquery-bin < 7:20170520
Provides:       tex-texosquery-doc = %{epoch}:20180414-%{release}
Provides:       texlive-texosquery-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texosquery-doc < 7:20170520
License:        LPPL
Summary:        Cross-platform Java application to query OS information
Requires:       texlive-base texlive-kpathsea
Requires:       java-headless
BuildArch:      noarch

%description -n texlive-texosquery
This package provides a cross-platform Java application to
query OS information designed for use in TeX's shell escape
mechanism. The application can query the following: locale and
codeset current working directory user home directory temporary
directory OS name, arch and version Current date and time in
PDF format (for TeX formats that don't provide
\pdfcreationdate) Date-time stamp of a file in PDF format (for
TeX formats that don't provide \pdffilemoddate) Size of a file
in bytes (for TeX formats that don't provide \pdffilesize)
Contents of a directory (captured as a list) Directory contents
filtered by regular expression (captured as a list) URI of a
file Canonical path of a file All paths use a forward slash as
directory divider so results can be used, for example, in
commands like \includegraphics. There are files provided for
easy access in TeX documents: texosquery.tex: generic TeX code
texosquery.sty: LaTeX package This provides commands to run
texosquery using TeX's shell escape mechanism and capture the
result in a control sequence. The category code of most of
TeX's default special characters (and some other potentially
problematic characters) is temporarily changed to 12 while
reading the result.

%package -n texlive-texsis
Provides:       tex-texsis = %{epoch}:20180414-%{release}
Provides:       tex-texsis-bin = %{epoch}:20180414-%{release}
Provides:       texlive-texsis-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texsis-bin < 7:20170520
Provides:       tex-texsis-doc = %{epoch}:20180414-%{release}
Provides:       texlive-texsis-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texsis-doc < 7:20170520
License:        LPPL
Summary:        Plain TeX macros for PhysicistsRequires:       texlive-base
Requires:       texlive-kpathsea texlive-pdftex
Requires:       texlive-tetex texlive-tex
Requires(post,postun): coreutils
Provides:       tex(TXSconts.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSdcol.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSenvmt.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSeqns.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSfigs.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSfmts.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSfonts.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXShead.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSinit.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSletr.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSmacs.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSmemo.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSprns.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSrefs.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSruled.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSsects.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSsite.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXSsymb.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXStags.tex) = %{epoch}:20180414-%{release}
Provides:       tex(TXStitle.tex) = %{epoch}:20180414-%{release}
Provides:       tex(texsis.tex) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-texsis
TeXsis is a TeX macro package which provides useful features
for typesetting research papers and related documents. For
example, it includes support specifically for: Automatic
numbering of equations, figures, tables and references;
Simplified control of type sizes, line spacing, footnotes,
running headlines and footlines, and tables of contents,
figures and tables; Specialized document formats for research
papers, preprints and ``e-prints,'' conference proceedings,
theses, books, referee reports, letters, and memoranda;
Simplified means of constructing an index for a book or thesis;
Easy to use double column formatting; Specialized environments
for lists, theorems and proofs, centered or non-justified text,
and listing computer code; Specialized macros for easily
constructing ruled tables. TeXsis was originally developed for
physicists, but others may also find it useful. It is
completely compatible with Plain TeX.

%package -n texlive-texware
Provides:       tex-texware = %{epoch}:20180414-%{release}
Provides:       tex-texware-bin = %{epoch}:20180414-%{release}
Provides:       texlive-texware-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-texware-bin < 7:20170520
License:        Knuth
Summary:        Utility programs for use with TeX
Requires:       texlive-base texlive-kpathsea

%description -n texlive-texware
Basic utitility programs, comprising: - dvitype, which converts
a TeX output (DVI) file to a plain text file (see also the DVI
Text Language suite); - pooltype, which converts a TeX-suite
program's "pool" (string) file into human-readable form; and -
tftopl and pltotf, which convert TeX Font Metric (TFM) file to
human readable Property List (PL) files and vice versa.

%package -n texlive-thumbpdf
Provides:       tex-thumbpdf = %{epoch}:20180414-%{release}
Provides:       tex-thumbpdf-bin = %{epoch}:20180414-%{release}
Provides:       texlive-thumbpdf-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-thumbpdf-bin < 7:20170520
Provides:       tex-thumbpdf-doc = %{epoch}:20180414-%{release}
Provides:       texlive-thumbpdf-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-thumbpdf-doc < 7:20170520
License:        LPPL
Summary:        Thumbnails for pdfTeX and dvips/ps2pdf
Requires:       texlive-base texlive-kpathsea
Requires:       tex(ifluatex.sty) ghostscript
Provides:       tex(thumbpdf.sty) = %{epoch}:20180414-%{release}
Provides:       tex(thumbpdf.tex) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-thumbpdf
A Perl script that provides support for thumbnails in pdfTeX
and dvips/ps2pdf. The script uses ghostscript to generate the
thumbnails which get represented in a TeX readable file that is
read by the package thumbpdf.sty to automatically include the
thumbnails. This arrangement works with both plain TeX and
LaTeX.

%package -n texlive-tie
Provides:       tex-tie = %{epoch}:20180414-%{release} tex-tie-bin = %{epoch}:20180414-%{release}
Provides:       texlive-tie-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-tie-bin < 7:20170520
License:        Latex2e
Summary:        Allow multiple web change files
Requires:       texlive-base texlive-kpathsea

%description -n texlive-tie
Tie was originally developed to allow web programmers to apply
more than one change file to their source. The program may also
be used to create a new version of a .web file that
incorporates existing changes.

%package -n texlive-tpic2pdftex
Provides:       tex-tpic2pdftex = %{epoch}:20180414-%{release}
Provides:       tex-tpic2pdftex-bin = %{epoch}:20180414-%{release}
Provides:       texlive-tpic2pdftex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-tpic2pdftex-bin < 7:20170520
Provides:       tex-tpic2pdftex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-tpic2pdftex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-tpic2pdftex-doc < 7:20170520
License:        GPL+
Summary:        Use tpic commands in PDFTeX
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-tpic2pdftex
The AWK script converts pic language, embedded inline
(delimited by .PS and .PE markers), to \pdfliteral commands.

%package -n texlive-ttfutils
Provides:       tex-ttfutils = %{epoch}:20180414-%{release}
Provides:       tex-ttfutils-bin = %{epoch}:20180414-%{release}
Provides:       texlive-ttfutils-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ttfutils-bin < 7:20170520
Provides:       tex-ttfutils-doc = %{epoch}:20180414-%{release}
Provides:       texlive-ttfutils-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ttfutils-doc < 7:20170520
License:        LPPL
Summary:        Linux TrueType utilities
Requires:       texlive-base texlive-kpathsea
Provides:       tex(T1-WGL4.enc) = %{epoch}:20180414-%{release}
Provides:       tex(ttf2pk.cfg) = %{epoch}:20180414-%{release}

%description -n texlive-ttfutils
Linux TrueType utilities.

%package -n texlive-typeoutfileinfo
Provides:       tex-typeoutfileinfo = %{epoch}:20180414-%{release}
Provides:       tex-typeoutfileinfo-bin = %{epoch}:20180414-%{release}
Provides:       texlive-typeoutfileinfo-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-typeoutfileinfo-bin < 7:20170520
Provides:       tex-typeoutfileinfo-doc = %{epoch}:20180414-%{release}
Provides:       texlive-typeoutfileinfo-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-typeoutfileinfo-doc < 7:20170520
License:        LPPL 1.3
Summary:        Display class/package/file information
Requires:       texlive-base texlive-kpathsea
Requires:       tex(readprov.sty)
BuildArch:      noarch

%description -n texlive-typeoutfileinfo
The package provides a minimalist shell script, for Unix
systems, that displays the information content in a
\ProvidesFile, \ProvidesPackage or \ProvidesClass command in a
LaTeX source file. The package requires that the readprov
package is available.

%package -n texlive-ulqda
Provides:       tex-ulqda = %{epoch}:20180414-%{release}
Provides:       tex-ulqda-bin = %{epoch}:20180414-%{release}
Provides:       texlive-ulqda-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ulqda-bin < 7:20170520
Provides:       tex-ulqda-doc = %{epoch}:20180414-%{release}
Provides:       texlive-ulqda-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-ulqda-doc < 7:20170520
License:        LPPL
Summary:        Support of Qualitative Data Analysis
Requires:       texlive-base texlive-kpathsea
Requires:       tex(multicol.sty) tex(tikz.sty)
Requires:       tex(dot2texi.sty) tex(soul.sty)
Provides:       tex(ulqda.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-ulqda
The package is for use in Qualitative Data Analysis research.
It supports the integration of Qualitative Data Analysis (QDA)
research tasks, specifically for Grounded Theory, into the
LaTeX work flow. It assists in the analysis of textual data
such as interview transcripts and field notes by providing the
LaTeX user with macros which are used to markup textual
information -- for example, in-depth interviews.

%package -n texlive-uptex
Provides:       tex-uptex = %{epoch}:20180414-%{release}
Provides:       tex-uptex-bin = %{epoch}:20180414-%{release}
Provides:       tex-uptex-doc = %{epoch}:20180414-%{release}
Provides:       tex-uplatex = %{epoch}:20180414-%{release}
Provides:       tex-uplatex-bin = %{epoch}:20180414-%{release}
Provides:       tex-uplatex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-uptex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-uptex-bin < 7:20170520
Provides:       texlive-uplatex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-uplatex-bin < 7:20170520
Provides:       texlive-uplatex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-uplatex-doc < 7:20170520
Provides:       texlive-uptex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-uptex-doc < 7:20170520
License:        BSD
Summary:        Binaries for uptex
Requires:       texlive-base texlive-convbkmk
Requires:       texlive-hyph-utf8 texlive-ipaex
Requires:       texlive-japanese texlive-japanese-otf
Requires:       texlive-kpathsea texlive-ptex

%description -n texlive-uptex
upTeX is an extension of pTeX, using UTF-8 input and producing UTF-8
output. It was originally designed to improve support for Japanese,
but is also useful for documents in Chinese and Korean. It can
process Chinese simplified, Chinese traditional, Japanese, and Korean
simultaneously, and can also produce original LaTeX with \inputenc{utf8}
and Babel (Latin/Cyrillic/Greek etc.) by switching its \kcatcode
tables.

%package -n texlive-urlbst
Provides:       tex-urlbst = %{epoch}:20180414-%{release}
Provides:       tex-urlbst-bin = %{epoch}:20180414-%{release}
Provides:       texlive-urlbst-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-urlbst-bin < 7:20170520
Provides:       tex-urlbst-doc = %{epoch}:20180414-%{release}
Provides:       texlive-urlbst-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-urlbst-doc < 7:20170520
License:        GPL+
Summary:        Web support for BibTeX
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-urlbst
Supports a new BibTeX 'webpage' entry type and 'url',
'lastchecked', and 'eprint' and 'DOI' fields. The Perl script
urlbst can be used to add this support to an arbitrary .bst
file which has a reasonably conventional structure. The result
is meant to be robust rather than pretty.

%package -n texlive-velthuis
Provides:       tex-velthuis = %{epoch}:20180414-%{release}
Provides:       tex-velthuis-bin = %{epoch}:20180414-%{release}
Provides:       texlive-velthuis-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-velthuis-bin < 7:20170520
Provides:       tex-velthuis-doc = %{epoch}:20180414-%{release}
Provides:       texlive-velthuis-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-velthuis-doc < 7:20170520
Provides:       texlive-devnag = %{epoch}:20180414-%{release}
Obsoletes:      texlive-devnag < 7:20170520
Provides:       texlive-devnag-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-devnag-bin < 7:20170520
License:        GPL+
Summary:        Typeset Devanagari
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-tetex tex-xetex-devanagari
Requires:       tex(hindicaptions.sty) tex(cite.sty)
Requires:       tex(ifxetex.sty)
Provides:       tex(dvng.map) = %{epoch}:20180414-%{release}
Provides:       tex(dvnb10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnb8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnb9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbb10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbb8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbb9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbbi10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbbi8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbbi9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbi10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbi8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbi9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnc10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnc8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnc9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvncb10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvncb8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvncb9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvncbi10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvncbi8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvncbi9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnci10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnci8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnci9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvng10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvng8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvng9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvngb10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvngb8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvngb9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvngbi10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvngbi8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvngbi9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvngi10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvngi8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvngi9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnn10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnn8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnn9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnnb10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnnb8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnnb9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnnbi10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnnbi8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnnbi9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnni10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnni8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnni9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvpb10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvpb8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvpb9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvpc10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvpc8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvpc9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvpn10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvpn8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvpn9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvpnn10.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvpnn8.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvpnn9.tfm) = %{epoch}:20180414-%{release}
Provides:       tex(dvnb10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnb8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnb9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbb10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbb8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbb9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbbi10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbbi8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbbi9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbi10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbi8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnbi9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnc10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnc8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnc9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvncb10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvncb8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvncb9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvncbi10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvncbi8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvncbi9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnci10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnci8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnci9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvng10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvng8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvng9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvngb10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvngb8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvngb9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvngbi10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvngbi8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvngbi9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvngi10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvngi8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvngi9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnn10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnn8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnn9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnnb10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnnb8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnnb9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnnbi10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnnbi8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnnbi9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnni10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnni8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvnni9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvpb10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvpb8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvpb9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvpc10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvpc8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvpc9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvpn10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvpn8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvpn9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvpnn10.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvpnn8.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(dvpnn9.pfb) = %{epoch}:20180414-%{release}
Provides:       tex(hindi.ldf) = %{epoch}:20180414-%{release}
Provides:       tex(hindi.sty) = %{epoch}:20180414-%{release}
Provides:       tex(dev.sty) = %{epoch}:20180414-%{release}
Provides:       tex(dev209.sty) = %{epoch}:20180414-%{release}
Provides:       tex(devanagari.sty) = %{epoch}:20180414-%{release}
Provides:       tex(dvngcite.sty) = %{epoch}:20180414-%{release}
Provides:       tex(udn.fd) = %{epoch}:20180414-%{release}
Provides:       tex(udnb.fd) = %{epoch}:20180414-%{release}
Provides:       tex(udnc.fd) = %{epoch}:20180414-%{release}
Provides:       tex(udnn.fd) = %{epoch}:20180414-%{release}
Provides:       tex(udnp.fd) = %{epoch}:20180414-%{release}
Provides:       tex(udnpb.fd) = %{epoch}:20180414-%{release}
Provides:       tex(udnpc.fd) = %{epoch}:20180414-%{release}
Provides:       tex(udnpn.fd) = %{epoch}:20180414-%{release}
Provides:       tex(dnmacs.tex) = %{epoch}:20180414-%{release}
Provides:       tex(hindicaptions.sty) = %{epoch}:20180414-%{release}

%description -n texlive-velthuis
Frans Velthuis' preprocessor for Devanagari text, and fonts and
macros to use when typesetting the processed text. The macros
provide features that support Sanskrit, Hindi, Marathi, Nepali,
and other languages typically printed in the Devanagari script.
The package provides fonts, in both Metafont and Type 1
formats. Users of modern TeX distributions may care to try the
XeTeX based package, which is far preferable for users who can
type Unicode text.

%package -n texlive-vlna
Provides:       tex-vlna = %{epoch}:20180414-%{release} tex-vlna-bin = %{epoch}:20180414-%{release}
Provides:       texlive-vlna-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-vlna-bin < 7:20170520
Provides:       tex-vlna-doc = %{epoch}:20180414-%{release}
Provides:       texlive-vlna-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-vlna-doc < 7:20170520
License:        LPPL
Summary:        Adds tilde after each non-syllabic preposition
Requires:       texlive-base texlive-kpathsea

%description -n texlive-vlna
There exists a special Czech and Slovak typographical rule:
you cannot leave the non-syllabic preposition on the end of one
line and continue writting text on next line. For example, you
cannot write down the text "v lese" (in a forest) like
"v<new-line>lese". The program vlna adds the asciitilde between
such preposition and the next word and removes the space(s) in
this place.  It means, the program converts "v lese" to
"v~lese". You can use this program as a preporcessor before
TeXing. Moreower, you can set another sequence to store instead
asciitilte (see the -x option).

%package -n texlive-vpe
Provides:       tex-vpe = %{epoch}:20180414-%{release} tex-vpe-bin = %{epoch}:20180414-%{release}
Provides:       texlive-vpe-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-vpe-bin < 7:20170520
Provides:       tex-vpe-doc = %{epoch}:20180414-%{release}
Provides:       texlive-vpe-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-vpe-doc < 7:20170520
License:        LPPL
Summary:        Source specials for PDF output
Requires:       texlive-base texlive-kpathsea
Requires:       tex(keyval.sty) tex(color.sty)
Requires:       tex(pifont.sty)
Provides:       tex(vpe.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-vpe
VPE is a system to make the equivalent of "source special"
marks in a PDF file. Clicking on a mark will activate an
editor, pointing at the source line that produced the text that
was marked. The system comprises a perl file (vpe.pl) and a
LaTeX package (vpe.sty); it will work with PDF files generated
via LaTeX/dvips, pdfTeX (version 0.14 or better), and
LaTeX/VTeX. Using the LaTeX/dvips or pdfLaTeX routes, the
(pdf)TeX processor should be run with shell escapes enabled.

%package -n texlive-web
Provides:       tex-web = %{epoch}:20180414-%{release} tex-web-bin = %{epoch}:20180414-%{release}
Provides:       texlive-web-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-web-bin < 7:20170520
License:        Knuth
Summary:        Original web programs tangle and weave
Requires:       texlive-base texlive-kpathsea

%description -n texlive-web
The system processes 'web' files in two ways: firstly to
rearrange them to produce compilable code (using the program
tangle), and secondly to produce a TeX source (using the
program weave) that may be typeset for comfortable reading.

%package -n texlive-wordcount
Provides:       tex-wordcount = %{epoch}:20180414-%{release}
Provides:       texlive-wordcount-bin = %{epoch}:20180414-%{release}
Provides:       tex-wordcount-doc = %{epoch}:20180414-%{release}
Provides:       texlive-wordcount-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-wordcount-doc < 7:20180414
Provides:       tex(wordcount.tex) = %{epoch}:20180414-%{release}
License:        LPPL
Summary:        Estimate the number of words in a LaTeX document
Requires:       texlive-base texlive-kpathsea
BuildArch:      noarch

%description -n texlive-wordcount
The package provides a relatively easy way of estimating the
number of words in a LaTeX document that does not require
dvitty or other DVI converters. It does however require
something like Unix grep -c that can search a file for a
particular string and report the number of matching lines. An
accompanying shell script wordcount.sh contains more
information in its comments.

%package -n texlive-xdvi
License:        MIT
Summary:        A DVI previewer for the X Window System
Provides:       tex-xdvi = %{epoch}:20180414-%{release} tex-xdvi-bin = %{epoch}:20180414-%{release}
Provides:       texlive-xdvi-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-xdvi-bin < 7:20170520
Provides:       xdvi = %{epoch}:20180414-%{release} xdvik = %{epoch}:20180414-%{release}
Requires:       texlive-kpathsea texlive-base

%description -n texlive-xdvi
The canonical previewer for use on Unix and other X-windows
based systems.

%package -n texlive-xetex
Provides:       tex-xetex = %{epoch}:20180414-%{release}
Provides:       tex-xetex-bin = %{epoch}:20180414-%{release}
Provides:       texlive-xetex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-xetex-bin < 7:20170520
Provides:       tex-xetex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-xetex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-xetex-doc < 7:20170520
License:        MIT
Summary:        Unicode and OpenType-enabled TeX engine
Requires:       texlive-base texlive-kpathsea
Requires:       texlive-tetex texlive-xetexconfig
Requires(post,postun): coreutils
Requires:       tex(xetex.def)
Provides:       tex(qx-unicode.map) = %{epoch}:20180414-%{release}
Provides:       tex(tex-text.map) = %{epoch}:20180414-%{release}

%description -n texlive-xetex
XeTeX is an extension of TeX that integrates TeX's typesetting capabilities
with (a) the Unicode text encoding standard (supporting most of the world’s
scripts) and (b) modern font technologies (TrueType and OpenType) and text
layout services (AAT, OpenType layout, SIL Graphite) provided by the host
operating system and available libraries.

With XeTeX, the advanced typographic features provided by OpenType fonts become
available for all TeX users, as well as support for complex non-roman scripts.
XeTeX also eliminates the complex task of managing a TeX font installation.
XeTeX is now part of the standard TeX distribution TeXLive and works well with
TeX macro packages like LaTeX and ConTeXt.

%ifarch empty
%package -n texlive-xindy
Provides:       tex-xindy = %{epoch}:20180414-%{release}
Provides:       tex-xindy-bin = %{epoch}:20180414-%{release}
Provides:       tex-xindy-doc = %{epoch}:20180414-%{release}
Provides:       texlive-xindy-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-xindy-bin <= 6:svn41316
Provides:       tex-xindy-doc = %{epoch}:20180414-%{release}
Provides:       texlive-xindy-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-xindy-doc <= 6:svn41316
License:        GPLv2+
Summary:        A general-purpose index processor
Requires:       texlive-base texlive-kpathsea

%description -n texlive-xindy
Xindy was deceloped after an impasse had been encountered in
the attempt to complete internationalisation of makeindex.
Xindy can be used to process indexes for documents marked up
using (La)TeX, Nroff family and SGML-based languages. Xindy is
highly configurable, both in markup terms and in terms of the
collating order of the text being processed.
%endif

%package -n texlive-xmltex
Provides:       tex-xmltex = %{epoch}:20180414-%{release}
Provides:       tex-xmltex-bin = %{epoch}:20180414-%{release}
Provides:       texlive-xmltex-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-xmltex-bin < 7:20170520
Provides:       tex-xmltex-doc = %{epoch}:20180414-%{release}
Provides:       texlive-xmltex-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-xmltex-doc < 7:20170520
Provides:       xmltex = %{epoch}:20180414-%{release}
License:        LPPL
Summary:        Support for parsing XML documents
Requires:       texlive-base texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-latex texlive-pdftex
Requires:       texlive-tetex texlive-tex
Requires:       texlive-xmltexconfig
Provides:       tex(xmltex.cfg) = %{epoch}:20180414-%{release}
Provides:       tex(xmltex.tex) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-xmltex
The package provides an implementation of a parser for
documents matching the XML 1.0 and XML Namespace
Recommendations. In addition to parsing commands are provided
to attatch TeX typesetting instructions to the various markup
elemenets as they are encounted. Sample files for typesetting a
subset of TEI, MathML, are included. Element and Attribute
names, as well as character data, may use any characters
allowed in XML, using UTF-8 or a suitable 8-bit encoding.

%package -n texlive-yplan
Provides:       tex-yplan = %{epoch}:20180414-%{release}
Provides:       tex-yplan-bin = %{epoch}:20180414-%{release}
Provides:       texlive-yplan-bin = %{epoch}:20180414-%{release}
Obsoletes:      texlive-yplan-bin < 7:20170520
Provides:       tex-yplan-doc = %{epoch}:20180414-%{release}
Provides:       texlive-yplan-doc = %{epoch}:20180414-%{release}
Obsoletes:      texlive-yplan-doc < 7:20170520
License:        LPPL
Summary:        Daily planner type calendar
Requires:       texlive-base texlive-kpathsea
Requires:       tex(ifthen.sty)
Provides:       tex(yplan.sty) = %{epoch}:20180414-%{release}
BuildArch:      noarch

%description -n texlive-yplan
Prints two six-monthly vertical-type daily planner (i.e.,
months along the top, days downwards), with each 6-month period
fitting onto a single A4 (or US letter) sheet. The package
offers support for English, French, German, Spanish and
Portuguese. The previous scheme of annual updates has now been
abandoned, in favour of a Perl script yplan that generates a
year's planner automatically. (The last manually-generated
LaTeX file remains on the archive.)

%prep
%autosetup -c -n texlive-20180414-source -p1
[ -e texlive-20180414-source ] && mv texlive-20180414-source source

for l in `unxz -c %{SOURCE3} | tar t`; do
ln -s %{_datadir}/texlive/licenses/$l $l
done

%global mysources %{lua: for index,value in ipairs(sources) do if index >= 16 then print(value.." ") end end}

%ifarch loongarch64
sed -i '/fmt=pdfimage/d' source/texk/web2c/pdftexdir/pdfimage.test
sed -i '14d' source/texk/web2c/pdftexdir/pdftosrc.test
sed -i '/src\/test-13/d' source/texk/web2c/pdftexdir/pdftosrc.test
sed -i '/pdftosrc test-13.pdf/d' source/texk/web2c/pdftexdir/pdftosrc.test
sed -i '/test-13.xref/d' source/texk/web2c/pdftexdir/pdftosrc.test
%endif

%build
export CFLAGS="$RPM_OPT_FLAGS -fno-strict-aliasing -Werror=format-security -fcommon"
export CXXFLAGS="$RPM_OPT_FLAGS -std=c++11 -fno-strict-aliasing -Werror=format-security -fcommon"
export LDFLAGS="%{build_ldflags}"
cd source
PREF=`pwd`/inst
install -d work
%global _configure ../configure
cd work
%configure \
--prefix=$PREF --datadir=$PREF --libdir=$PREF/lib --includedir=$PREF/include --datarootdir=$PREF/share --mandir=$PREF/share/man \
--infodir=$PREF/share/info --exec_prefix=$PREF --bindir=$PREF/bin --with-system-zlib --with-system-libpng \
--with-system-gd --without-system-t1lib --without-system-teckit --with-system-freetype2 --with-system-zziplib \
--with-system-cairo --with-system-icu --with-system-harfbuzz --with-system-graphite2 --with-system-libgs --with-system-pixman \
--with-system-libpaper --without-system-potrace --with-pic --with-xdvi-x-toolkit=xaw --with-system-mpfr --with-system-gmp \
--enable-shared --enable-compiler-warnings=max --without-cxx-runtime-hack \
--disable-native-texlive-build --disable-t1utils --disable-psutils --disable-biber --disable-ptexenc --disable-largefile \
--disable-xindy --disable-xindy-docs --disable-xindy-make-rules \
%ifarch aarch64 loongarch64
--disable-luajittex --disable-mfluajit \
%endif
--disable-rpath

for i in `find . -name libtool`; do
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' $i
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' $i
done

%make_build world STRIPPROG=/bin/true STRIP=/bin/true

%install
install -d %{buildroot}%{_datadir}/texlive/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf

cd %{buildroot}%{_datadir}/texlive/texmf-config/web2c
ln -s ../../texmf-dist/web2c/updmap.cfg updmap.cfg
cd -

cd %{buildroot}%{_datadir}
install -d texlive/texmf-local/texmf-compat
ln -s texlive/texmf-local/texmf-compat texmf
cd -

install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
for i in public/lilyglyphs ; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_datadir}/texlive/texmf-dist/fonts/opentype/$i $j
done
cd -

install -d %{buildroot}%{_bindir}
rm -f source/inst/bin/man
cp -a source/inst/bin/* %{buildroot}%{_bindir}

install -d %{buildroot}%{_libdir}
cp -d source/inst/lib/*.so* %{buildroot}%{_libdir}
cp -a source/inst/lib/pkgconfig %{buildroot}%{_libdir}

install -d %{buildroot}%{_includedir}
cp -r source/inst/include/* %{buildroot}%{_includedir}

install -d %{buildroot}%{_datadir}
install -d %{buildroot}%{_datadir}/texlive
cd source/inst/share
cp -a info %{buildroot}%{_datadir}/
cp -a man %{buildroot}%{_datadir}/
cp -a texmf-dist %{buildroot}%{_datadir}/texlive/
cd -

cd %{buildroot}%{_bindir}
for i in `find . -type l`; do
if [ "`readlink $i | grep '..' | wc -l`" == "1" ]; then
l=`readlink $i | sed s,.*texmf,/usr/share/texlive/texmf,`
rm -f $i
ln -s $l $i
fi
done
cd -

cd %{buildroot}%{_datadir}/texlive
echo %{mysources}
for noarchsrc in %{mysources}; do
  xz -dc $noarchsrc | tar x
done
cd -

cd %{buildroot}%{_datadir}/texlive/texmf-dist
xz -dc %{SOURCE5} | tar x
xz -dc %{SOURCE6} | tar x
xz -dc %{SOURCE7} | tar x
xz -dc %{SOURCE8} | tar x
xz -dc %{SOURCE9} | tar x
xz -dc %{SOURCE10} | tar x
xz -dc %{SOURCE11} | tar x
xz -dc %{SOURCE12} | tar x
xz -dc %{SOURCE13} | tar x
xz -dc %{SOURCE14} | tar x
cd -

cp -a source/texk/kpathsea/texmf.cnf %{buildroot}%{_datadir}/texlive/texmf-dist/web2c/texmf.cnf

sed -i 's|\\sc |\\scshape |g' %{buildroot}%{_datadir}/texlive/texmf-dist/bibtex/bst/base/acm.bst
sed -i 's|\\sc |\\scshape |g' %{buildroot}%{_datadir}/texlive/texmf-dist/bibtex/bst/base/siam.bst

install -d %{buildroot}%{_sysconfdir}/texlive/web2c
install -d %{buildroot}%{_sysconfdir}/texlive/dvips/config
install -d %{buildroot}%{_sysconfdir}/texlive/tex/generic/config


mv %{buildroot}%{_datadir}/texlive/texmf-dist/web2c/mktex.cnf %{buildroot}%{_sysconfdir}/texlive/web2c/
ln -s %{_sysconfdir}/texlive/web2c/mktex.cnf %{buildroot}%{_datadir}/texlive/texmf-dist/web2c/mktex.cnf
mv %{buildroot}%{_datadir}/texlive/texmf-dist/web2c/texmf.cnf %{buildroot}%{_sysconfdir}/texlive/web2c/
ln -s %{_sysconfdir}/texlive/web2c/texmf.cnf %{buildroot}%{_datadir}/texlive/texmf-dist/web2c/texmf.cnf
mv %{buildroot}%{_datadir}/texlive/texmf-dist/web2c/updmap.cfg %{buildroot}%{_sysconfdir}/texlive/web2c/
ln -s %{_sysconfdir}/texlive/web2c/updmap.cfg %{buildroot}%{_datadir}/texlive/texmf-dist/web2c/updmap.cfg


sed -i -e 's|^TEXMFLOCAL.*|TEXMFLOCAL = $TEXMFROOT/texmf-local//|' %{buildroot}%{_sysconfdir}/texlive/web2c/texmf.cnf

mv %{buildroot}%{_datadir}/texlive/texmf-dist/dvips/config/config.ps %{buildroot}%{_sysconfdir}/texlive/dvips/config/
ln -s %{_sysconfdir}/texlive/dvips/config/config.ps %{buildroot}%{_datadir}/texlive/texmf-dist/dvips/config/config.ps

mv %{buildroot}%{_datadir}/texlive/texmf-dist/web2c/fmtutil.cnf %{buildroot}%{_sysconfdir}/texlive/web2c/fmtutil.cnf
sed -i '/^[a-z].*$/s/^/\#\!\ /' %{buildroot}%{_sysconfdir}/texlive/web2c/fmtutil.cnf

mkdir %{buildroot}%{_datadir}/texlive/fmtutil.cnf.d
for i in $(grep '^# from .*:$' %{buildroot}%{_sysconfdir}/texlive/web2c/fmtutil.cnf|sed 's/^# from //; s/:$//'); do
    echo "#" > %{buildroot}%{_datadir}/texlive/fmtutil.cnf.d/$i
    sed -n "s/^#! //; /^# from $i:\$/,/^#\$/{/^#\$/!p}" %{buildroot}%{_sysconfdir}/texlive/web2c/fmtutil.cnf >> %{buildroot}%{_datadir}/texlive/fmtutil.cnf.d/$i
done

install -D -p -m 755 -t %{buildroot}%{_sbindir} %{SOURCE4}

install -d %{buildroot}%{_rpmmacrodir}
cp -a %{SOURCE1} %{buildroot}%{_rpmmacrodir}/macros.texlive

cp %{SOURCE2} %{buildroot}%{_datadir}/texlive

install -d %{buildroot}%{_datadir}/texlive/licenses
cd %{buildroot}%{_datadir}/texlive/licenses
xz -dc %{SOURCE3} | tar x
cd -

rm -rf %{buildroot}%{_datadir}/texlive/texmf-dist/doc/man/man*/*.pdf
rm -rf %{buildroot}%{_datadir}/texlive/texmf-dist/doc/man/Makefile
rm -rf %{buildroot}%{_datadir}/texlive/texmf-dist/doc/man/man*/Makefile
rm -rf %{buildroot}%{_datadir}/texlive/texmf-dist/doc/info/dir
rm -rf %{buildroot}%{_datadir}/texlive/texmf-dist/doc/man/man1/tlmgr.1

cd %{buildroot}%{_datadir}/texlive
rm -rf texmf-var
ln -s %{_var}/lib/texmf texmf-var
cd -

cd %{buildroot}%{_bindir}
[ ! -e mfplain ] && ln -s mpost mfplain
[ ! -e texlua ] && ln -s luatex texlua
[ ! -e texluac ] && ln -s luatex texluac

rm -f latexmk
rm -rf %{buildroot}%{_datadir}/texlive/texmf-dist/scripts/latexmk
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/doc/man/man1/latexmk.*

rm -rf %{buildroot}%{_bindir}/teckit_compile

rm -f bibexport.sh
ln -s /usr/share/texlive/texmf-dist/scripts/bibexport/bibexport.sh bibexport.sh
rm -f texmfstart
ln -s /usr/share/texlive/texmf-dist/scripts/context/ruby/texmfstart.rb texmfstart
rm -f context
cat > context << EOF
export TEXMF=/usr/share/texlive/texmf-dist;
export TEXMFCNF=/usr/share/texlive/texmf-dist/web2c;
export TEXMFCACHE=\$HOME/.cache/texlive;
%{_bindir}/mtxrun --script context "\$@"
EOF
chmod 0755 context
cd -

install -d %{buildroot}%{_datadir}/
install -d %{buildroot}%{_infodir}/
cp -R %{buildroot}%{_datadir}/texlive/texmf-dist/doc/man %{buildroot}%{_datadir}/
find %{buildroot}%{_datadir}/texlive/texmf-dist/doc/man -type f | xargs rm -f
mv %{buildroot}%{_datadir}/texlive/texmf-dist/doc/info/* %{buildroot}%{_infodir}/

for file in $(find %{buildroot}%{_libdir}/pkgconfig/ -type f -name '*.pc')
do sed -i 's|%{_builddir}/%{name}-%{version}/source/inst|/usr|g' $file
   sed -i 's|/usr/lib|%{_libdir}|g' $file
done

cd %{buildroot}
find -type f -exec sed -i '1s|^#!/usr/bin/python$|#!%{__python3}|' {} +
find -type f -exec sed -i '1s|^#!/usr/bin/env python$|#!%{__python3}|' {} +
sed -i '1s|^#!/usr/bin/python |#!%{__python3} |' ./%{_datadir}/texlive/texmf-dist/scripts/de-macro/de-macro
cd -

file `find %{buildroot}/%{_bindir} -type f` | grep -w ELF | awk -F: '{print $1}' | xargs chrpath -d
file `find %{buildroot}/%{_libdir} -type f` | grep -w ELF | awk -F: '{print $1}' | xargs chrpath -d

mkdir -p %{buildroot}/etc/ld.so.conf.d
echo "/home/abuild/rpmbuild/BUILD/texlive-20180414-source/source/inst/lib" > %{buildroot}/etc/ld.so.conf.d/%{name}-%{_arch}.conf

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%pretrans -p <lua>
path = "/usr/share/texmf"
st = posix.stat(path)
if st and st.type == "directory" then
  status = os.rename(path, path .. ".rpmmoved")
  if not status then
    suffix = 0
    while not status do
      suffix = suffix + 1
      status = os.rename(path .. ".rpmmoved", path .. ".rpmmoved." .. suffix)
    end
    os.rename(path, path .. ".rpmmoved")
  end
end

%pre
rm -rf %{_datadir}/texlive/texmf-var
rm -rf %{_var}/lib/texmf/*
:

%posttrans
if [ -x /usr/sbin/selinuxenabled ] && /usr/sbin/selinuxenabled; then
[ -x /sbin/restorecon ] && /sbin/restorecon -R %{_var}/lib/texmf/
fi
:

%transfiletriggerin -n texlive-kpathsea -- %{_datadir}/texlive
%{_bindir}/texhash 2> /dev/null || :
export TEXMF=/usr/share/texlive/texmf-dist
export TEXMFCNF=/usr/share/texlive/texmf-dist/web2c
export TEXMFCACHE=/var/lib/texmf
%{_bindir}/mtxrun --generate &> /dev/null || :
%{_bindir}/fmtutil-sys --all &> /dev/null || :

%transfiletriggerpostun -n texlive-kpathsea -- %{_datadir}/texlive
%{_bindir}/texhash 2> /dev/null || :

%transfiletriggerin -n texlive-kpathsea -- %{_datadir}/texlive/texmf-dist/fonts/map/dvips/
list=`grep "\.map" | sort -n | uniq`
while read -r line; do
        [ -z "$line" ] && continue
        shortfile=`basename "$line"`
        if `echo $shortfile | grep -Eq 'allrunes.map|arabtex.map|arss.map|artm.map|bbold.map|cbgreek-full.map|ccpl.map|cmextra.map|cmll.map|cm.map|cm-super-t1.map|cm-super-t2a.map|cm-super-t2b.map|cm-super-t2c.map|cm-super-ts1.map|cm-super-x2.map|cmtext-bsr-interpolated.map|cyrillic.map|dvng.map|esint.map|ethiop.map|eurosym.map|hfbright.map|iby.map|latxfont.map|lxfonts.map|manfnt.map|mflogo.map|mongolian.map|musix.map|pigpen.map|plother.map|pltext.map|rsfs.map|semaf.map|stmaryrd.map|symbols.map|tipa.map|trajan.map|vnrother.map|vnrtext.map|wasy.map|xypic.map|yhmath.map'`; then
                %{_bindir}/updmap-sys --nomkmap --enable MixedMap=$shortfile >/dev/null 2>&1 || :
        else
                %{_bindir}/updmap-sys --nomkmap --enable Map=$shortfile >/dev/null 2>&1 || :
        fi
done <<< "$list"
%{_bindir}/updmap-sys --quiet --nomkmap >/dev/null || :

%transfiletriggerpostun -n texlive-kpathsea -- %{_datadir}/texlive/texmf-dist/fonts/map/dvips/
list=`grep "\.map" | sort -n | uniq`
while read -r line; do
        [ -z "$line" ] && continue
        shortfile=`basename "$line"`
        if `echo $shortfile | grep -Eq 'allrunes.map|arabtex.map|arss.map|artm.map|bbold.map|cbgreek-full.map|ccpl.map|cmextra.map|cmll.map|cm.map|cm-super-t1.map|cm-super-t2a.map|cm-super-t2b.map|cm-super-t2c.map|cm-super-ts1.map|cm-super-x2.map|cmtext-bsr-interpolated.map|cyrillic.map|dvng.map|esint.map|ethiop.map|eurosym.map|hfbright.map|iby.map|latxfont.map|lxfonts.map|manfnt.map|mflogo.map|mongolian.map|musix.map|pigpen.map|plother.map|pltext.map|rsfs.map|semaf.map|stmaryrd.map|symbols.map|tipa.map|trajan.map|vnrother.map|vnrtext.map|wasy.map|xypic.map|yhmath.map'`; then
                %{_bindir}/updmap-sys --nomkmap --disable MixedMap=$shortfile >/dev/null 2>&1 || :
        else
                %{_bindir}/updmap-sys --nomkmap --disable Map=$shortfile >/dev/null 2>&1 || :
        fi
done <<< "$list"
%{_bindir}/updmap-sys --quiet --nomkmap >/dev/null || :

%transfiletriggerin -n texlive-kpathsea -P 2000000 -- %{_datadir}/texlive/fmtutil.cnf.d/
%{_sbindir}/generate-fmtutilcnf %{_datadir}/texlive

%transfiletriggerpostun -n texlive-kpathsea -P 2000000 -- %{_datadir}/texlive/fmtutil.cnf.d/
%{_sbindir}/generate-fmtutilcnf %{_datadir}/texlive

%files
%{_datadir}/texlive/licenses/
%{_datadir}/texlive/texlive.tlpdb
%{_rpmmacrodir}/macros.texlive
%dir %{_sysconfdir}/texlive
%dir %{_sysconfdir}/texlive/dvips
%dir %{_sysconfdir}/texlive/dvips/config
%dir %{_sysconfdir}/texlive/tex
%dir %{_sysconfdir}/texlive/tex/generic
%dir %{_sysconfdir}/texlive/tex/generic/config
%dir %{_sysconfdir}/texlive/web2c
%dir %{_datadir}/texlive
%dir %{_datadir}/texlive/texmf-dist
%dir %{_datadir}/texlive/texmf-dist/bibtex/
%dir %{_datadir}/texlive/texmf-dist/bibtex/csf
%dir %{_datadir}/texlive/texmf-dist/bibtex/csf/base
%dir %{_datadir}/texlive/texmf-dist/doc
%dir %{_datadir}/texlive/texmf-dist/doc/info
%dir %{_datadir}/texlive/texmf-dist/doc/man
%dir %{_datadir}/texlive/texmf-dist/doc/man/man1
%dir %{_datadir}/texlive/texmf-dist/doc/man/man5
%dir %{_datadir}/texlive/texmf-dist/dvips
%dir %{_datadir}/texlive/texmf-dist/dvips/config
%dir %{_datadir}/texlive/texmf-dist/fonts
%dir %{_datadir}/texlive/texmf-dist/fonts/cmap
%dir %{_datadir}/texlive/texmf-dist/fonts/enc
%dir %{_datadir}/texlive/texmf-dist/fonts/enc/dvips
%dir %{_datadir}/texlive/texmf-dist/fonts/map
%dir %{_datadir}/texlive/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texlive/texmf-dist/fonts/map/glyphlist
%dir %{_datadir}/texlive/texmf-dist/fonts/sfd
%dir %{_datadir}/texlive/texmf-dist/scripts
%dir %{_datadir}/texlive/texmf-dist/scripts/texlive
%dir %{_datadir}/texlive/texmf-dist/source
%dir %{_datadir}/texlive/texmf-dist/source/fonts
%dir %{_datadir}/texlive/texmf-dist/source/fonts/zhmetrics
%dir %{_datadir}/texlive/texmf-dist/texconfig
%dir %{_datadir}/texlive/texmf-dist/web2c
%dir %{_var}/lib/texmf
%{_datadir}/texlive/texmf-var
%{_datadir}/texlive/texmf-local/
%{_datadir}/texmf
%config(noreplace) /etc/ld.so.conf.d/*
%ghost %{_datadir}/texmf.rpmmoved
%exclude %{_datadir}/texlive/install-tl
%exclude %{_datadir}/texlive/tlpkg/gpg/
%exclude %{_datadir}/texlive/tlpkg/tlpobj/
%exclude %{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/
%exclude %{_datadir}/texlive/texmf-dist/scripts/texlive/tlmgr.pl
%exclude %{_datadir}/texlive/texmf-dist/scripts/texlive/tlmgrgui.pl
%exclude %{_datadir}/texlive/texmf-dist/scripts/texlive/uninstall-win32.pl
%exclude %{_datadir}/texlive/texmf-dist/scripts/tlcockpit/tlcockpit.sh
%exclude %{_datadir}/texlive/texmf-dist/scripts/tlshell/tlshell.tcl
%exclude %{_datadir}/texlive/tlpkg/installer/config.guess
%exclude %{_datadir}/texlive/tlpkg/installer/COPYING.MinGW-runtime.txt
%exclude %{_datadir}/texlive/tlpkg/installer/ctan-mirrors.pl
%exclude %{_datadir}/texlive/tlpkg/installer/install-menu-extl.pl
%exclude %{_datadir}/texlive/tlpkg/installer/install-menu-perltk.pl
%exclude %{_datadir}/texlive/tlpkg/installer/install-menu-text.pl
%exclude %{_datadir}/texlive/tlpkg/installer/install-menu-wizard.pl
%exclude %{_datadir}/texlive/tlpkg/installer/texlive.png
%exclude %{_bindir}/tlcockpit
%exclude %{_bindir}/tlmgr
%exclude %{_bindir}/tlshell
%exclude %{_datadir}/info/dir
%exclude %{_datadir}/texlive/readme-txt.dir/README.*
%exclude %{_includedir}/ptexenc
%exclude %{_datadir}/texlive/texmf-dist/source/fonts/zhmetrics/ttfonts.map
%exclude %{_mandir}/man1/xindy.1*
%exclude %{_mandir}/man1/texindy.1*
%exclude %{_mandir}/man1/tex2xindy.1*
%exclude %{_datadir}/texlive/texmf-dist/scripts/xindy
%exclude %{_datadir}/texlive/texmf-dist/xindy
%exclude %{_datadir}/texlive/texmf-dist/doc/xindy
%exclude %{_bindir}/cjk-gs-integrate
%exclude %{_datadir}/texlive/texmf-dist/scripts/cjk-gs-integrate
%exclude %{_datadir}/texlive/texmf-dist/doc/fonts/cjk-gs-integrate
%exclude %{_datadir}/texlive/texmf-dist/fonts/misc/cjk-gs-integrate

%files -n texlive-a2ping
%license gpl.txt
%{_bindir}/a2ping
%{_datadir}/texlive/texmf-dist/scripts/a2ping/
%{_mandir}/man1/a2ping.1*
%doc %{_datadir}/texlive/texmf-dist/doc/support/a2ping/

%files -n texlive-accfonts
%license gpl.txt
%{_bindir}/mkt1font
%{_bindir}/vpl2ovp
%{_bindir}/vpl2vpl
%{_datadir}/texlive/texmf-dist/scripts/accfonts/
%{_datadir}/texlive/texmf-dist/tex/latex/accfonts/
%doc %{_datadir}/texlive/texmf-dist/doc/fonts/accfonts/

%files -n texlive-adhocfilelist
%license lppl1.txt
%{_bindir}/adhocfilelist
%{_datadir}/texlive/texmf-dist/scripts/adhocfilelist/
%{_datadir}/texlive/texmf-dist/tex/support/adhocfilelist/
%doc %{_datadir}/texlive/texmf-dist/doc/support/adhocfilelist/

%files -n texlive-afm2pl
%license lppl1.txt
%{_bindir}/afm2pl
%{_mandir}/man1/afm2pl.1*
%{_datadir}/texlive/texmf-dist/fonts/enc/dvips/afm2pl/
%{_datadir}/texlive/texmf-dist/fonts/lig/afm2pl/
%{_datadir}/texlive/texmf-dist/tex/fontinst/afm2pl/

%files -n texlive-aleph
%license gpl.txt
%{_bindir}/aleph
%{_bindir}/lamed
%{_mandir}/man1/aleph.1*
%{_mandir}/man1/lamed.1*
%{_datadir}/texlive/fmtutil.cnf.d/aleph
%doc %{_datadir}/texlive/texmf-dist/doc/aleph/

%files -n texlive-amstex
%license lppl1.txt
%{_bindir}/amstex
%{_mandir}/man1/amstex.1*
%{_datadir}/texlive/texmf-dist/tex/amstex/base/
%{_datadir}/texlive/texmf-dist/tex/amstex/config/
%{_datadir}/texlive/fmtutil.cnf.d/amstex
%doc %{_datadir}/texlive/texmf-dist/doc/amstex/base/

%files -n texlive-arara
%license bsd.txt
%{_bindir}/arara
%{_datadir}/texlive/texmf-dist/scripts/arara/
%doc %{_datadir}/texlive/texmf-dist/doc/support/arara/

%files -n texlive-authorindex
%license lppl1.txt
%{_bindir}/authorindex
%{_datadir}/texlive/texmf-dist/scripts/authorindex/
%{_datadir}/texlive/texmf-dist/tex/latex/authorindex/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/authorindex/

%files -n texlive-autosp
%license gpl2.txt
%{_bindir}/autosp
%{_bindir}/tex2aspc
%{_mandir}/man1/autosp.1*
%{_mandir}/man1/tex2aspc.1*
%doc %{_datadir}/texlive/texmf-dist/doc/generic/autosp/

%files -n texlive-axodraw2
%license gpl3.txt
%{_bindir}/axohelp
%{_mandir}/man1/axohelp.1*
%{_datadir}/texlive/texmf-dist/tex/latex/axodraw2/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/axodraw2/

%files -n texlive-bib2gls
%license gpl3.txt
%{_bindir}/bib2gls
%{_bindir}/convertgls2bib
%{_datadir}/texlive/texmf-dist/scripts/bib2gls/
%doc %{_datadir}/texlive/texmf-dist/doc/support/bib2gls/

%files -n texlive-bibexport
%license lppl1.3.txt
%{_bindir}/bibexport
%{_bindir}/bibexport.sh
%{_datadir}/texlive/texmf-dist/bibtex/bst/bibexport/
%{_datadir}/texlive/texmf-dist/scripts/bibexport/
%doc %{_datadir}/texlive/texmf-dist/doc/bibtex/bibexport/

%files -n texlive-bibtex
%license knuth.txt
%{_bindir}/bibtex
%{_mandir}/man1/bibtex.1*
%{_datadir}/texlive/texmf-dist/bibtex/bib/base/xampl.bib
%{_datadir}/texlive/texmf-dist/bibtex/bst/base/abbrv.bst
%{_datadir}/texlive/texmf-dist/bibtex/bst/base/acm.bst
%{_datadir}/texlive/texmf-dist/bibtex/bst/base/alpha.bst
%{_datadir}/texlive/texmf-dist/bibtex/bst/base/apalike.bst
%{_datadir}/texlive/texmf-dist/bibtex/bst/base/ieeetr.bst
%{_datadir}/texlive/texmf-dist/bibtex/bst/base/plain.bst
%{_datadir}/texlive/texmf-dist/bibtex/bst/base/siam.bst
%{_datadir}/texlive/texmf-dist/bibtex/bst/base/unsrt.bst
%doc %{_datadir}/texlive/texmf-dist/doc/bibtex/base/README
%doc %{_datadir}/texlive/texmf-dist/doc/bibtex/base/btxbst.doc
%doc %{_datadir}/texlive/texmf-dist/doc/bibtex/base/btxdoc.bib
%doc %{_datadir}/texlive/texmf-dist/doc/bibtex/base/btxdoc.pdf
%doc %{_datadir}/texlive/texmf-dist/doc/bibtex/base/btxdoc.tex
%doc %{_datadir}/texlive/texmf-dist/doc/bibtex/base/btxhak.pdf
%doc %{_datadir}/texlive/texmf-dist/doc/bibtex/base/btxhak.tex
%{_datadir}/texlive/texmf-dist/tex/generic/bibtex/apalike.sty
%{_datadir}/texlive/texmf-dist/tex/generic/bibtex/apalike.tex

%files -n texlive-bibtexu
%license lppl1.txt
%{_bindir}/bibtexu
%doc %{_datadir}/texlive/texmf-dist/doc/bibtexu/

%files -n texlive-bibtex8
%license gpl.txt
%{_bindir}/bibtex8
%{_datadir}/texlive/texmf-dist/bibtex/csf/base/88591lat.csf
%{_datadir}/texlive/texmf-dist/bibtex/csf/base/88591sca.csf
%{_datadir}/texlive/texmf-dist/bibtex/csf/base/README.TEXLIVE
%{_datadir}/texlive/texmf-dist/bibtex/csf/base/ascii.csf
%{_datadir}/texlive/texmf-dist/bibtex/csf/base/cp437lat.csf
%{_datadir}/texlive/texmf-dist/bibtex/csf/base/cp850lat.csf
%{_datadir}/texlive/texmf-dist/bibtex/csf/base/cp850sca.csf
%{_datadir}/texlive/texmf-dist/bibtex/csf/base/cp866rus.csf
%{_datadir}/texlive/texmf-dist/bibtex/csf/base/csfile.txt
%{_datadir}/texlive/texmf-dist/bibtex/csf/polish-csf/88592pl.csf
%{_datadir}/texlive/texmf-dist/bibtex/csf/polish-csf/cp1250pl.csf
%{_datadir}/texlive/texmf-dist/bibtex/csf/polish-csf/cp852pl.csf
%{_datadir}/texlive/texmf-dist/bibtex/csf/polish-csf/iso8859-7.csf
%doc %{_datadir}/texlive/texmf-dist/doc/bibtex8/

%files -n texlive-bundledoc
%license lppl1.txt
%{_bindir}/arlatex
%{_bindir}/bundledoc
%{_mandir}/man1/arlatex.1*
%{_mandir}/man1/bundledoc.1*
%{_datadir}/texlive/texmf-dist/scripts/bundledoc/
%{_datadir}/texlive/texmf-dist/tex/latex/bundledoc/
%doc %{_datadir}/texlive/texmf-dist/doc/support/bundledoc/

%files -n texlive-cachepic
%license lppl1.3.txt
%{_bindir}/cachepic
%{_datadir}/texlive/texmf-dist/scripts/cachepic/
%{_datadir}/texlive/texmf-dist/tex/latex/cachepic/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/cachepic/

%files -n texlive-checkcites
%license lppl1.3.txt
%{_bindir}/checkcites
%{_datadir}/texlive/texmf-dist/scripts/checkcites/
%doc %{_datadir}/texlive/texmf-dist/doc/support/checkcites/

%files -n texlive-checklistings
%license lppl1.2.txt
%{_bindir}/checklistings
%{_datadir}/texlive/texmf-dist/scripts/checklistings/
%{_datadir}/texlive/texmf-dist/tex/latex/checklistings/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/checklistings/

%files -n texlive-chktex
%license gpl.txt
%{_bindir}/chktex
%{_bindir}/chkweb
%{_bindir}/deweb
%{_mandir}/man1/chktex.1*
%{_mandir}/man1/chkweb.1*
%{_mandir}/man1/deweb.1*
%{_datadir}/texlive/texmf-dist/chktex/
%{_datadir}/texlive/texmf-dist/scripts/chktex/
%doc %{_datadir}/texlive/texmf-dist/doc/chktex/

%files -n texlive-cjkutils
%license lppl1.txt
%{_bindir}/bg5+latex
%{_bindir}/bg5+pdflatex
%{_bindir}/bg5conv
%{_bindir}/bg5latex
%{_bindir}/bg5pdflatex
%{_bindir}/cef5conv
%{_bindir}/cef5latex
%{_bindir}/cef5pdflatex
%{_bindir}/cefconv
%{_bindir}/ceflatex
%{_bindir}/cefpdflatex
%{_bindir}/cefsconv
%{_bindir}/cefslatex
%{_bindir}/cefspdflatex
%{_bindir}/extconv
%{_bindir}/gbklatex
%{_bindir}/gbkpdflatex
%{_bindir}/hbf2gf
%{_bindir}/sjisconv
%{_bindir}/sjislatex
%{_bindir}/sjispdflatex
%{_mandir}/man1/bg5conv.1*
%{_mandir}/man1/cef5conv.1*
%{_mandir}/man1/cefconv.1*
%{_mandir}/man1/cefsconv.1*
%{_mandir}/man1/extconv.1*
%{_mandir}/man1/hbf2gf.1*
%{_mandir}/man1/sjisconv.1*
%{_datadir}/texlive/texmf-dist/hbf2gf/

%files -n texlive-context
%{_bindir}/context
%{_bindir}/contextjit
%{_bindir}/luatools
%{_bindir}/mtxrun
%{_bindir}/mtxrunjit
%{_bindir}/texexec
%{_bindir}/texmfstart
%{_mandir}/man1/context.1*
%{_mandir}/man1/luatools.1*
%{_mandir}/man1/mtx-babel.1*
%{_mandir}/man1/mtx-base.1*
%{_mandir}/man1/mtx-bibtex.1*
%{_mandir}/man1/mtx-cache.1*
%{_mandir}/man1/mtx-chars.1*
%{_mandir}/man1/mtx-check.1*
%{_mandir}/man1/mtx-colors.1*
%{_mandir}/man1/mtx-context.1*
%{_mandir}/man1/mtx-dvi.1*
%{_mandir}/man1/mtx-epub.1*
%{_mandir}/man1/mtx-evohome.1*
%{_mandir}/man1/mtx-fcd.1*
%{_mandir}/man1/mtx-flac.1*
%{_mandir}/man1/mtx-fonts.1*
%{_mandir}/man1/mtx-grep.1*
%{_mandir}/man1/mtx-interface.1*
%{_mandir}/man1/mtx-metapost.1*
%{_mandir}/man1/mtx-metatex.1*
%{_mandir}/man1/mtx-modules.1*
%{_mandir}/man1/mtx-package.1*
%{_mandir}/man1/mtx-patterns.1*
%{_mandir}/man1/mtx-pdf.1*
%{_mandir}/man1/mtx-plain.1*
%{_mandir}/man1/mtx-profile.1*
%{_mandir}/man1/mtx-rsync.1*
%{_mandir}/man1/mtx-scite.1*
%{_mandir}/man1/mtx-server.1*
%{_mandir}/man1/mtx-texworks.1*
%{_mandir}/man1/mtx-timing.1*
%{_mandir}/man1/mtx-tools.1*
%{_mandir}/man1/mtx-unicode.1*
%{_mandir}/man1/mtx-unzip.1*
%{_mandir}/man1/mtx-update.1*
%{_mandir}/man1/mtx-watch.1*
%{_mandir}/man1/mtx-youless.1*
%{_mandir}/man1/mtxrun.1*
%{_mandir}/man1/texexec.1*
%{_mandir}/man1/texmfstart.1*
%{_datadir}/texlive/texmf-dist/bibtex/bst/context/
%{_datadir}/texlive/texmf-dist/context/
%{_datadir}/texlive/texmf-dist/fonts/afm/hoekwater/context/contnav.afm
%{_datadir}/texlive/texmf-dist/fonts/cid/fontforge/Adobe-CNS1-4.cidmap
%{_datadir}/texlive/texmf-dist/fonts/cid/fontforge/Adobe-GB1-4.cidmap
%{_datadir}/texlive/texmf-dist/fonts/cid/fontforge/Adobe-Identity-0.cidmap
%{_datadir}/texlive/texmf-dist/fonts/cid/fontforge/Adobe-Japan1-5.cidmap
%{_datadir}/texlive/texmf-dist/fonts/cid/fontforge/Adobe-Japan1-6.cidmap
%{_datadir}/texlive/texmf-dist/fonts/cid/fontforge/Adobe-Japan2-0.cidmap
%{_datadir}/texlive/texmf-dist/fonts/cid/fontforge/Adobe-Korea1-2.cidmap
%{_datadir}/texlive/texmf-dist/fonts/enc/dvips/context/
%{_datadir}/texlive/texmf-dist/fonts/map/dvips/context/
%{_datadir}/texlive/texmf-dist/fonts/map/luatex/context/
%{_datadir}/texlive/texmf-dist/fonts/map/pdftex/context/
%{_datadir}/texlive/texmf-dist/fonts/misc/xetex/fontmapping/context/
%{_datadir}/texlive/texmf-dist/fonts/tfm/hoekwater/context/
%{_datadir}/texlive/texmf-dist/fonts/type1/hoekwater/context/
%{_datadir}/texlive/texmf-dist/metapost/context/
%{_datadir}/texlive/texmf-dist/scripts/context/
%{_datadir}/texlive/texmf-dist/tex/context/
%{_datadir}/texlive/texmf-dist/tex/generic/context/
%{_datadir}/texlive/texmf-dist/tex/latex/context/
%{_datadir}/texlive/fmtutil.cnf.d/context
%doc %{_datadir}/texlive/texmf-dist/doc/context/
%exclude %{_datadir}/texlive/texmf-dist/scripts/context/stubs/mswin
%exclude %{_datadir}/texlive/texmf-dist/scripts/context/stubs/win64
%exclude %{_datadir}/texlive/texmf-dist/scripts/context/stubs/source

%files -n texlive-convbkmk
%{_bindir}/convbkmk
%{_datadir}/texlive/texmf-dist/scripts/convbkmk/
%doc %{_datadir}/texlive/texmf-dist/doc/support/convbkmk/

%files -n texlive-crossrefware
%license gpl.txt
%{_bindir}/bbl2bib
%{_bindir}/bibdoiadd
%{_bindir}/bibmradd
%{_bindir}/biburl2doi
%{_bindir}/bibzbladd
%{_bindir}/ltx2crossrefxml
%{_mandir}/man1/bbl2bib.1*
%{_mandir}/man1/bibdoiadd.1*
%{_mandir}/man1/bibmradd.1*
%{_mandir}/man1/biburl2doi.1*
%{_mandir}/man1/bibzbladd.1*
%{_mandir}/man1/ltx2crossrefxml.1*
%{_datadir}/texlive/texmf-dist/scripts/crossrefware/
%{_datadir}/texlive/texmf-dist/tex/latex/crossrefware/
%doc %{_datadir}/texlive/texmf-dist/doc/support/crossrefware/

%files -n texlive-cslatex
%license gpl.txt
%{_bindir}/cslatex
%{_bindir}/pdfcslatex
%{_datadir}/texlive/texmf-dist/tex/cslatex/
%{_datadir}/texlive/fmtutil.cnf.d/cslatex

%files -n texlive-csplain
%{_bindir}/csplain
%{_bindir}/pdfcsplain
%{_datadir}/texlive/texmf-dist/tex/csplain/
%{_datadir}/texlive/fmtutil.cnf.d/csplain

%files -n texlive-ctan-o-mat
%license bsd.txt
%{_bindir}/ctan-o-mat
%{_mandir}/man1/ctan-o-mat.1*
%{_datadir}/texlive/texmf-dist/scripts/ctan-o-mat/
%doc %{_datadir}/texlive/texmf-dist/doc/support/ctan-o-mat/

%files -n texlive-ctanify
%license lppl1.3.txt
%{_bindir}/ctanify
%{_mandir}/man1/ctanify.1*
%{_datadir}/texlive/texmf-dist/scripts/ctanify/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/ctanify/

%files -n texlive-ctanupload
%license gpl3.txt
%{_bindir}/ctanupload
%{_datadir}/texlive/texmf-dist/scripts/ctanupload/
%doc %{_datadir}/texlive/texmf-dist/doc/support/ctanupload/

%files -n texlive-ctie
%license gpl.txt
%{_bindir}/ctie
%{_mandir}/man1/ctie.1*

%files -n texlive-cweb
%license knuth.txt
%{_bindir}/ctangle
%{_bindir}/cweave
%{_mandir}/man1/ctangle.1*
%{_mandir}/man1/cweave.1*
%{_mandir}/man1/cweb.1*
%{_datadir}/texlive/texmf-dist/tex/plain/cweb/
%doc %{_datadir}/texlive/texmf-dist/doc/plain/cweb/

%files -n texlive-cyrillic
%license lppl1.3.txt
%{_bindir}/rubibtex
%{_bindir}/rumakeindex
%{_mandir}/man1/rubibtex.1*
%{_mandir}/man1/rumakeindex.1*
%{_datadir}/texlive/texmf-dist/tex/latex/cyrillic/
%{_datadir}/texlive/texmf-dist/scripts/texlive/rubibtex.sh
%{_datadir}/texlive/texmf-dist/scripts/texlive/rumakeindex.sh
%doc %{_datadir}/texlive/texmf-dist/doc/latex/cyrillic/

%files -n texlive-de-macro
%{_bindir}/de-macro
%{_datadir}/texlive/texmf-dist/scripts/de-macro/
%doc %{_datadir}/texlive/texmf-dist/doc/support/de-macro/

%files -n texlive-detex
%{_bindir}/detex
%{_mandir}/man1/detex.1*

%files -n texlive-diadia
%license lppl1.txt
%{_bindir}/diadia
%{_datadir}/texlive/texmf-dist/scripts/diadia/
%{_datadir}/texlive/texmf-dist/tex/latex/diadia/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/diadia/

%files -n texlive-dosepsbin
%{_bindir}/dosepsbin
%{_mandir}/man1/dosepsbin.1*
%{_datadir}/texlive/texmf-dist/scripts/dosepsbin/
%doc %{_datadir}/texlive/texmf-dist/doc/support/dosepsbin/

%files -n texlive-dtl
%license pd.txt
%{_bindir}/dt2dv
%{_bindir}/dv2dt
%{_mandir}/man1/dt2dv.1*
%{_mandir}/man1/dv2dt.1*

%files -n texlive-dtxgen
%license gpl.txt
%{_bindir}/dtxgen
%{_datadir}/texlive/texmf-dist/scripts/dtxgen/
%doc %{_datadir}/texlive/texmf-dist/doc/support/dtxgen/

%files -n texlive-dvi2tty
%license gpl.txt
%{_bindir}/disdvi
%{_bindir}/dvi2tty
%{_mandir}/man1/disdvi.1*
%{_mandir}/man1/dvi2tty.1*

%files -n texlive-dviasm
%license gpl3.txt
%{_bindir}/dviasm
%{_datadir}/texlive/texmf-dist/scripts/dviasm/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/dviasm/

%files -n texlive-dvicopy
%license gpl.txt
%{_bindir}/dvicopy
%{_mandir}/man1/dvicopy.1*

%files -n texlive-dvidvi
%{_bindir}/dvidvi
%{_mandir}/man1/dvidvi.1*

%files -n texlive-dviinfox
%{_bindir}/dviinfox
%{_datadir}/texlive/texmf-dist/scripts/dviinfox/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/dviinfox/

%files -n texlive-dviljk
%license gpl.txt
%{_bindir}/dvihp
%{_bindir}/dvilj
%{_bindir}/dvilj2p
%{_bindir}/dvilj4
%{_bindir}/dvilj4l
%{_bindir}/dvilj6
%{_mandir}/man1/dvihp.1*
%{_mandir}/man1/dvilj.1*
%{_mandir}/man1/dvilj2p.1*
%{_mandir}/man1/dvilj4.1*
%{_mandir}/man1/dvilj4l.1*
%{_mandir}/man1/dvilj6.1*

%files -n texlive-dvipdfmx
%license gpl.txt
%{_bindir}/dvipdfm
%{_bindir}/dvipdfmx
%{_bindir}/dvipdft
%{_bindir}/ebb
%{_bindir}/extractbb
%{_mandir}/man1/dvipdfm.1*
%{_mandir}/man1/dvipdfmx.1*
%{_mandir}/man1/dvipdft.1*
%{_mandir}/man1/ebb.1*
%{_mandir}/man1/extractbb.1*
%{_mandir}/man1/xdvipdfmx.1*
%{_datadir}/texlive/texmf-dist/dvipdfmx/
%{_datadir}/texlive/texmf-dist/fonts/cmap/dvipdfmx/
%{_datadir}/texlive/texmf-dist/fonts/map/dvipdfmx/
%exclude %{_datadir}/texlive/texmf-dist/fonts/map/dvipdfmx/ptex-fontmaps/
%{_datadir}/texlive/tlpkg/tlpostcode/dvipdfmx.pl
%doc %{_datadir}/texlive/texmf-dist/doc/dvipdfm/
%doc %{_datadir}/texlive/texmf-dist/doc/dvipdfmx/

%files -n texlive-dvipng
%license lgpl2.1.txt
%{_bindir}/dvigif
%{_bindir}/dvipng
%{_mandir}/man1/dvigif.1*
%{_mandir}/man1/dvipng.1*
%{_infodir}/dvipng.info*
%doc %{_datadir}/texlive/texmf-dist/doc/dvipng/

%files -n texlive-dvipos
%license lppl1.txt
%{_bindir}/dvipos
%{_mandir}/man1/dvipos.1*

%files -n texlive-dvips
%license gpl.txt
%{_bindir}/afm2tfm
%{_bindir}/dvips
%{_mandir}/man1/afm2tfm.1*
%{_mandir}/man1/dvips.1*
%{_infodir}/dvips.info*
%{_datadir}/texlive/texmf-dist/dvips/base/
%{_datadir}/texlive/texmf-dist/dvips/config/alt-rule.pro
%{_datadir}/texlive/texmf-dist/dvips/config/canonex.cfg
%{_datadir}/texlive/texmf-dist/dvips/config/config.bakoma
%{_datadir}/texlive/texmf-dist/dvips/config/config.canonex
%{_datadir}/texlive/texmf-dist/dvips/config/config.cx
%{_datadir}/texlive/texmf-dist/dvips/config/config.deskjet
%{_datadir}/texlive/texmf-dist/dvips/config/config.dvired
%{_datadir}/texlive/texmf-dist/dvips/config/config.epson
%{_datadir}/texlive/texmf-dist/dvips/config/config.ibmvga
%{_datadir}/texlive/texmf-dist/dvips/config/config.ljfour
%{_datadir}/texlive/texmf-dist/dvips/config/config.luc
%{_datadir}/texlive/texmf-dist/dvips/config/config.mbn
%{_datadir}/texlive/texmf-dist/dvips/config/config.mga
%{_datadir}/texlive/texmf-dist/dvips/config/config.mirrorprint
%{_datadir}/texlive/texmf-dist/dvips/config/config.ot2
%config(noreplace) %{_sysconfdir}/texlive/dvips/config/config.ps
%{_datadir}/texlive/texmf-dist/dvips/config/config.ps
%{_datadir}/texlive/texmf-dist/dvips/config/config.qms
%{_datadir}/texlive/texmf-dist/dvips/config/config.toshiba
%{_datadir}/texlive/texmf-dist/dvips/config/config.unms
%{_datadir}/texlive/texmf-dist/dvips/config/config.xyp
%{_datadir}/texlive/texmf-dist/dvips/config/cx.cfg
%{_datadir}/texlive/texmf-dist/dvips/config/deskjet.cfg
%{_datadir}/texlive/texmf-dist/dvips/config/dfaxhigh.cfg
%{_datadir}/texlive/texmf-dist/dvips/config/dvired.cfg
%{_datadir}/texlive/texmf-dist/dvips/config/epson.cfg
%{_datadir}/texlive/texmf-dist/dvips/config/ibmvga.cfg
%{_datadir}/texlive/texmf-dist/dvips/config/ljfour.cfg
%{_datadir}/texlive/texmf-dist/dvips/config/qms.cfg
%{_datadir}/texlive/texmf-dist/dvips/config/toshiba.cfg
%{_datadir}/texlive/texmf-dist/fonts/enc/dvips/base/
%{_datadir}/texlive/texmf-dist/fonts/map/dvips/
%{_datadir}/texlive/texmf-dist/tex/generic/dvips/
%doc %{_datadir}/texlive/texmf-dist/doc/dvips/

%files -n texlive-dvisvgm
%license gpl.txt
%{_bindir}/dvisvgm
%{_mandir}/man1/dvisvgm.1*

%files -n texlive-ebong
%license pd.txt
%{_bindir}/ebong
%{_datadir}/texlive/texmf-dist/scripts/ebong/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/ebong/

%files -n texlive-eplain
%license gpl2.txt
%{_bindir}/eplain
%{_mandir}/man1/eplain.1*
%{_infodir}/eplain.info*
%{_datadir}/texlive/texmf-dist/tex/eplain/
%{_datadir}/texlive/fmtutil.cnf.d/eplain
%doc %{_datadir}/texlive/texmf-dist/doc/eplain/

%files -n texlive-epspdf
%license gpl.txt
%{_bindir}/epspdf
%{_bindir}/epspdftk
%{_infodir}/epspdf.info*
%{_datadir}/texlive/texmf-dist/scripts/epspdf/
%doc %{_datadir}/texlive/texmf-dist/doc/support/epspdf/

%files -n texlive-epstopdf
%{_bindir}/epstopdf
%{_bindir}/repstopdf
%{_mandir}/man1/epstopdf.1*
%{_mandir}/man1/repstopdf.1*
%{_datadir}/texlive/texmf-dist/scripts/epstopdf/
%doc %{_datadir}/texlive/texmf-dist/doc/support/epstopdf/

%files -n texlive-exceltex
%license gpl.txt
%{_bindir}/exceltex
%{_datadir}/texlive/texmf-dist/scripts/exceltex/
%{_datadir}/texlive/texmf-dist/tex/latex/exceltex/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/exceltex/

%files -n texlive-fig4latex
%license gpl3.txt
%{_bindir}/fig4latex
%{_datadir}/texlive/texmf-dist/scripts/fig4latex/
%doc %{_datadir}/texlive/texmf-dist/doc/support/fig4latex/

%files -n texlive-findhyph
%license gpl.txt
%{_bindir}/findhyph
%{_mandir}/man1/findhyph.1*
%{_datadir}/texlive/texmf-dist/scripts/findhyph/
%doc %{_datadir}/texlive/texmf-dist/doc/support/findhyph/

%files -n texlive-fontinst
%license lppl1.txt
%{_bindir}/fontinst
%{_mandir}/man1/fontinst.1*
%{_datadir}/texlive/texmf-dist/scripts/texlive/fontinst.sh
%{_datadir}/texlive/texmf-dist/tex/fontinst/
%{_datadir}/texlive/texmf-dist/tex/latex/fontinst/
%doc %{_datadir}/texlive/texmf-dist/doc/fonts/fontinst/

%files -n texlive-fontools
%license gpl2.txt
%{_bindir}/afm2afm
%{_bindir}/autoinst
%{_bindir}/ot2kpx
%{_mandir}/man1/afm2afm.1*
%{_mandir}/man1/autoinst.1*
%{_mandir}/man1/ot2kpx.1*
%{_datadir}/texlive/texmf-dist/fonts/enc/dvips/fontools/
%{_datadir}/texlive/texmf-dist/scripts/fontools/
%doc %{_datadir}/texlive/texmf-dist/doc/support/fontools/

%files -n texlive-fontware
%license lppl1.txt
%{_bindir}/pltotf
%{_bindir}/tftopl
%{_bindir}/vftovp
%{_bindir}/vptovf
%{_mandir}/man1/pltotf.1*
%{_mandir}/man1/tftopl.1*
%{_mandir}/man1/vftovp.1*
%{_mandir}/man1/vptovf.1*

%files -n texlive-fragmaster
%license gpl.txt
%{_bindir}/fragmaster
%{_datadir}/texlive/texmf-dist/scripts/fragmaster/
%doc %{_datadir}/texlive/texmf-dist/doc/support/fragmaster/

%files -n texlive-getmap
%license lppl1.txt
%{_bindir}/getmapdl
%{_datadir}/texlive/texmf-dist/scripts/getmap/
%{_datadir}/texlive/texmf-dist/tex/latex/getmap/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/getmap/

%files -n texlive-glossaries
%license lppl1.3.txt
%{_bindir}/makeglossaries
%{_bindir}/makeglossaries-lite
%{_mandir}/man1/makeglossaries.1*
%{_mandir}/man1/makeglossaries-lite.1*
%{_datadir}/texlive/texmf-dist/scripts/glossaries/
%{_datadir}/texlive/texmf-dist/tex/latex/glossaries/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/glossaries/

%files -n texlive-glyphlist
%{_datadir}/texlive/texmf-dist/fonts/map/glyphlist/

%files -n texlive-gregoriotex
%license gpl3.txt
%{_bindir}/gregorio
%{_datadir}/texlive/texmf-dist/scripts/gregoriotex/
%{_datadir}/texlive/texmf-dist/tex/lualatex/gregoriotex/
%{_datadir}/texlive/texmf-dist/tex/luatex/gregoriotex/
%{_datadir}/texlive/texmf-dist/fonts/source/gregoriotex/
%{_datadir}/texlive/texmf-dist/fonts/truetype/public/gregoriotex/
%doc %{_datadir}/texlive/texmf-dist/doc/luatex/gregoriotex/

%files -n texlive-gsftopk
%license gpl.txt
%{_bindir}/gsftopk
%{_mandir}/man1/gsftopk.1*
%{_datadir}/texlive/texmf-dist/dvips/gsftopk/

%files -n texlive-installfont
%license lppl1.txt
%{_bindir}/installfont-tl
%{_datadir}/texlive/texmf-dist/scripts/installfont/
%doc %{_datadir}/texlive/texmf-dist/doc/support/installfont/

%files -n texlive-jadetex
%{_bindir}/jadetex
%{_bindir}/pdfjadetex
%{_mandir}/man1/jadetex.1*
%{_mandir}/man1/pdfjadetex.1*
%{_datadir}/texlive/texmf-dist/tex/jadetex/
%{_datadir}/texlive/fmtutil.cnf.d/jadetex
%doc %{_datadir}/texlive/texmf-dist/doc/otherformats/jadetex/

%files -n texlive-jfmutil
%{_bindir}/jfmutil
%{_datadir}/texlive/texmf-dist/scripts/jfmutil/
%doc %{_datadir}/texlive/texmf-dist/doc/fonts/jfmutil/

%files -n texlive-kotex-utils
%license lppl1.txt
%{_bindir}/jamo-normalize
%{_bindir}/komkindex
%{_bindir}/ttf2kotexfont
%{_datadir}/texlive/texmf-dist/makeindex/kotex-utils/
%{_datadir}/texlive/texmf-dist/scripts/kotex-utils/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/kotex-utils/

%files -n texlive-kpathsea
%license lgpl2.1.txt
%{_bindir}/kpseaccess
%{_bindir}/kpsereadlink
%{_bindir}/kpsestat
%{_bindir}/kpsewhich
%{_bindir}/mkocp
%{_bindir}/mkofm
%{_bindir}/mktexfmt
%{_bindir}/mktexlsr
%{_bindir}/mktexmf
%{_bindir}/mktexpk
%{_bindir}/mktextfm
%{_bindir}/texhash
%{_sbindir}/generate-fmtutilcnf
%{_mandir}/man1/kpseaccess.1*
%{_mandir}/man1/kpsereadlink.1*
%{_mandir}/man1/kpsestat.1*
%{_mandir}/man1/kpsewhich.1*
%{_mandir}/man1/mkocp.1*
%{_mandir}/man1/mkofm.1*
%{_mandir}/man1/mktexfmt.1*
%{_mandir}/man1/mktexlsr.1*
%{_mandir}/man1/mktexmf.1*
%{_mandir}/man1/mktexpk.1*
%{_mandir}/man1/mktextfm.1*
%{_mandir}/man1/texhash.1*
%{_infodir}/kpathsea.info*
%{_infodir}/tds.info*
%{_infodir}/web2c.info*
%{_datadir}/texlive/texmf-dist/web2c/amiga-pl.tcx
%{_datadir}/texlive/texmf-dist/web2c/cp1250cs.tcx
%{_datadir}/texlive/texmf-dist/web2c/cp1250pl.tcx
%{_datadir}/texlive/texmf-dist/web2c/cp1250t1.tcx
%{_datadir}/texlive/texmf-dist/web2c/cp227.tcx
%{_datadir}/texlive/texmf-dist/web2c/cp852-cs.tcx
%{_datadir}/texlive/texmf-dist/web2c/cp852-pl.tcx
%{_datadir}/texlive/texmf-dist/web2c/cp8bit.tcx
%{_datadir}/texlive/texmf-dist/web2c/empty.tcx
%config(noreplace) %{_sysconfdir}/texlive/web2c/fmtutil.cnf
%ghost %{_datadir}/texlive/texmf-dist/web2c/fmtutil.cnf
%{_datadir}/texlive/texmf-dist/web2c/il1-t1.tcx
%{_datadir}/texlive/texmf-dist/web2c/il2-cs.tcx
%{_datadir}/texlive/texmf-dist/web2c/il2-pl.tcx
%{_datadir}/texlive/texmf-dist/web2c/il2-t1.tcx
%{_datadir}/texlive/texmf-dist/web2c/kam-cs.tcx
%{_datadir}/texlive/texmf-dist/web2c/kam-t1.tcx
%{_datadir}/texlive/texmf-dist/web2c/macce-pl.tcx
%{_datadir}/texlive/texmf-dist/web2c/macce-t1.tcx
%{_datadir}/texlive/texmf-dist/web2c/maz-pl.tcx
%config(noreplace) %{_sysconfdir}/texlive/web2c/mktex.cnf
%{_datadir}/texlive/texmf-dist/web2c/mktex.cnf
%{_datadir}/texlive/texmf-dist/web2c/mktex.opt
%{_datadir}/texlive/texmf-dist/web2c/mktexdir
%{_datadir}/texlive/texmf-dist/web2c/mktexdir.opt
%{_datadir}/texlive/texmf-dist/web2c/mktexnam
%{_datadir}/texlive/texmf-dist/web2c/mktexnam.opt
%{_datadir}/texlive/texmf-dist/web2c/mktexupd
%{_datadir}/texlive/texmf-dist/web2c/natural.tcx
%{_datadir}/texlive/texmf-dist/web2c/tcvn-t5.tcx
%config(noreplace) %{_sysconfdir}/texlive/web2c/texmf.cnf
%{_datadir}/texlive/texmf-dist/web2c/texmf.cnf
%{_datadir}/texlive/texmf-dist/web2c/viscii-t5.tcx
%dir %{_datadir}/texlive/fmtutil.cnf.d
%doc %{_datadir}/texlive/texmf-dist/doc/kpathsea/
%doc %{_datadir}/texlive/texmf-dist/doc/web2c/

%files -n texlive-l3build
%license lppl1.3.txt
%{_bindir}/l3build
%{_mandir}/man1/l3build.1*
%{_datadir}/texlive/texmf-dist/scripts/l3build/
%{_datadir}/texlive/texmf-dist/tex/latex/l3build/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/l3build/

%files -n texlive-lacheck
%license gpl.txt
%{_bindir}/lacheck
%{_mandir}/man1/lacheck.1*

%files -n texlive-latex
%license lppl1.3.txt
%{_bindir}/dvilualatex
%{_bindir}/latex
%{_bindir}/lualatex
%{_bindir}/pdflatex
%{_mandir}/man1/latex.1*
%{_mandir}/man1/pdflatex.1*
%{_datadir}/texlive/texmf-dist/makeindex/latex/
%{_datadir}/texlive/texmf-dist/tex/latex/base/
%{_datadir}/texlive/fmtutil.cnf.d/latex-bin
%doc %{_datadir}/texlive/texmf-dist/doc/latex/base/

%files -n texlive-latex-git-log
%license gpl3.txt
%{_bindir}/latex-git-log
%{_mandir}/man1/latex-git-log.1*
%{_datadir}/texlive/texmf-dist/scripts/latex-git-log/
%doc %{_datadir}/texlive/texmf-dist/doc/support/latex-git-log/

%files -n texlive-latex-papersize
%license apache2.txt
%{_bindir}/latex-papersize
%{_datadir}/texlive/texmf-dist/scripts/latex-papersize
%doc %{_datadir}/texlive/texmf-dist/doc/support/latex-papersize/

%files -n texlive-latex2man
%license lppl1.txt
%{_bindir}/latex2man
%{_mandir}/man1/latex2man.1*
%{_infodir}/latex2man.info*
%{_datadir}/texlive/texmf-dist/scripts/latex2man/
%{_datadir}/texlive/texmf-dist/tex/latex/latex2man/
%doc %{_datadir}/texlive/texmf-dist/doc/support/latex2man/

%files -n texlive-latex2nemeth
%license gpl3.txt
%{_bindir}/latex2nemeth
%{_datadir}/texlive/texmf-dist/scripts/latex2nemeth
%doc %{_datadir}/texlive/texmf-dist/doc/support/latex2nemeth

%files -n texlive-latexdiff
%license gpl3.txt
%{_bindir}/latexdiff
%{_bindir}/latexdiff-vc
%{_bindir}/latexrevise
%{_mandir}/man1/latexdiff-vc.1*
%{_mandir}/man1/latexdiff.1*
%{_mandir}/man1/latexrevise.1*
%{_datadir}/texlive/texmf-dist/scripts/latexdiff/
%doc %{_datadir}/texlive/texmf-dist/doc/support/latexdiff/

%files -n texlive-latexfileversion
%license lppl1.txt
%{_bindir}/latexfileversion
%{_datadir}/texlive/texmf-dist/scripts/latexfileversion/
%doc %{_datadir}/texlive/texmf-dist/doc/support/latexfileversion/

%files -n texlive-latexpand
%license bsd.txt
%{_bindir}/latexpand
%{_datadir}/texlive/texmf-dist/scripts/latexpand/
%doc %{_datadir}/texlive/texmf-dist/doc/support/latexpand/

%files -n texlive-latexindent
%license gpl3.txt
%{_bindir}/latexindent
%{_datadir}/texlive/texmf-dist/scripts/latexindent/
%doc %{_datadir}/texlive/texmf-dist/doc/support/latexindent/

%files -n texlive-lcdftypetools
%license gpl.txt
%{_bindir}/cfftot1
%{_bindir}/mmafm
%{_bindir}/mmpfb
%{_bindir}/otfinfo
%{_bindir}/otftotfm
%{_bindir}/t1dotlessj
%{_bindir}/t1lint
%{_bindir}/t1rawafm
%{_bindir}/t1reencode
%{_bindir}/t1testpage
%{_bindir}/ttftotype42
%{_mandir}/man1/cfftot1.1*
%{_mandir}/man1/mmafm.1*
%{_mandir}/man1/mmpfb.1*
%{_mandir}/man1/otfinfo.1*
%{_mandir}/man1/otftotfm.1*
%{_mandir}/man1/t1dotlessj.1*
%{_mandir}/man1/t1lint.1*
%{_mandir}/man1/t1rawafm.1*
%{_mandir}/man1/t1reencode.1*
%{_mandir}/man1/t1testpage.1*
%{_mandir}/man1/ttftotype42.1*

%files -n texlive-lib
%{_libdir}/*.so.*
%dir %{_datadir}/texlive/texmf-config
%dir %{_datadir}/texlive/texmf-config/web2c
%{_datadir}/texlive/texmf-config/web2c/updmap.cfg
%attr(0644, root, root) %verify(not md5 size mtime) %ghost %{_datadir}/texlive/texmf-config/ls-R

%files -n texlive-lib-devel
%dir %{_includedir}/kpathsea
%{_includedir}/kpathsea/*
%{_includedir}/synctex/
%{_includedir}/texlua52/
%{_includedir}/texlua53/
%ifnarch aarch64 loongarch64
%{_includedir}/texluajit/
%endif
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files -n texlive-lilyglyphs
%license lppl1.3.txt
%{_bindir}/lily-glyph-commands
%{_bindir}/lily-image-commands
%{_bindir}/lily-rebuild-pdfs
%{_datadir}/fonts/lilyglyphs
%{_datadir}/texlive/texmf-dist/fonts/opentype/public/lilyglyphs/
%{_datadir}/texlive/texmf-dist/scripts/lilyglyphs/
%{_datadir}/texlive/texmf-dist/tex/lualatex/lilyglyphs/
%doc %{_datadir}/texlive/texmf-dist/doc/lualatex/lilyglyphs/

%files -n texlive-listbib
%license gpl.txt
%{_bindir}/listbib
%{_datadir}/texlive/texmf-dist/bibtex/bst/listbib/
%{_datadir}/texlive/texmf-dist/scripts/listbib/
%{_datadir}/texlive/texmf-dist/tex/latex/listbib/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/listbib/

%files -n texlive-listings-ext
%license lppl1.2.txt
%{_bindir}/listings-ext.sh
%{_datadir}/texlive/texmf-dist/scripts/listings-ext/
%{_datadir}/texlive/texmf-dist/tex/latex/listings-ext/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/listings-ext/

%files -n texlive-lollipop
%license gpl3.txt
%{_bindir}/lollipop
%{_datadir}/texlive/texmf-dist/tex/lollipop/
%{_datadir}/texlive/fmtutil.cnf.d/lollipop
%doc %{_datadir}/texlive/texmf-dist/doc/otherformats/lollipop/

%files -n texlive-ltxfileinfo
%license gpl.txt
%{_bindir}/ltxfileinfo
%{_datadir}/texlive/texmf-dist/scripts/ltxfileinfo/
%doc %{_datadir}/texlive/texmf-dist/doc/support/ltxfileinfo/

%files -n texlive-ltximg
%license gpl2.txt
%{_bindir}/ltximg
%{_datadir}/texlive/texmf-dist/scripts/ltximg/
%doc %{_datadir}/texlive/texmf-dist/doc/support/ltximg/

%files -n texlive-lua2dox
%license lppl1.3.txt
%{_bindir}/lua2dox_filter
%{_datadir}/texlive/texmf-dist/scripts/lua2dox/
%doc %{_datadir}/texlive/texmf-dist/doc/support/lua2dox/

%files -n texlive-luaotfload
%license gpl2.txt
%{_bindir}/luaotfload-tool
%{_mandir}/man1/luaotfload-tool.1*
%{_mandir}/man5/luaotfload.conf.5*
%{_datadir}/texlive/texmf-dist/scripts/luaotfload/
%{_datadir}/texlive/texmf-dist/tex/luatex/luaotfload/
%doc %{_datadir}/texlive/texmf-dist/doc/luatex/luaotfload/

%files -n texlive-luatex
%license gpl2.txt
%{_bindir}/dviluatex
%ifnarch aarch64 loongarch64
%{_bindir}/luajittex
%{_bindir}/texluajit
%{_bindir}/texluajitc
%endif
%{_bindir}/luatex
%{_bindir}/luatex53
%{_bindir}/texlua
%{_bindir}/texlua53
%{_bindir}/texluac
%{_mandir}/man1/luatex.1*
%{_mandir}/man1/texlua.1*
%{_mandir}/man1/texluac.1*
%{_datadir}/texlive/texmf-dist/tex/generic/config/luatex-unicode-letters.tex
%{_datadir}/texlive/texmf-dist/tex/generic/config/luatexiniconfig.tex
%{_datadir}/texlive/texmf-dist/web2c/texmfcnf.lua
%{_datadir}/texlive/fmtutil.cnf.d/luatex
%doc %{_datadir}/texlive/texmf-dist/doc/luatex/base/

%files -n texlive-lwarp
%license lppl1.3.txt
%{_bindir}/lwarpmk
%{_datadir}/texlive/texmf-dist/scripts/lwarp
%{_datadir}/texlive/texmf-dist/tex/latex/lwarp
%doc %{_datadir}/texlive/texmf-dist/doc/latex/lwarp

%files -n texlive-lyluatex
%{_datadir}/texlive/texmf-dist/scripts/lyluatex/
%{_datadir}/texlive/texmf-dist/tex/luatex/lyluatex/
%doc %{_datadir}/texlive/texmf-dist/doc/support/lyluatex/

%files -n texlive-make4ht
%license lppl1.3.txt
%{_bindir}/make4ht
%{_datadir}/texlive/texmf-dist/scripts/make4ht/
%doc %{_datadir}/texlive/texmf-dist/doc/support/make4ht/

%files -n texlive-makedtx
%license lppl1.txt
%{_bindir}/makedtx
%{_datadir}/texlive/texmf-dist/scripts/makedtx/
%{_datadir}/texlive/texmf-dist/tex/latex/makedtx/
%doc %{_datadir}/texlive/texmf-dist/doc/support/makedtx/

%files -n texlive-makeindex
%{_bindir}/makeindex
%{_bindir}/mkindex
%{_mandir}/man1/makeindex.1*
%{_mandir}/man1/mkindex.1*
%{_datadir}/texlive/texmf-dist/makeindex/
%{_datadir}/texlive/texmf-dist/tex/plain/makeindex/
%doc %{_datadir}/texlive/texmf-dist/doc/support/makeindex/

%files -n texlive-match_parens
%license gpl.txt
%{_bindir}/match_parens
%{_datadir}/texlive/texmf-dist/scripts/match_parens/
%doc %{_datadir}/texlive/texmf-dist/doc/support/match_parens/

%files -n texlive-mathspic
%license lppl1.txt
%{_bindir}/mathspic
%{_mandir}/man1/mathspic.1*
%{_datadir}/texlive/texmf-dist/scripts/mathspic/
%{_datadir}/texlive/texmf-dist/tex/latex/mathspic/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/mathspic/

%files -n texlive-metafont
%license knuth.txt
%{_bindir}/inimf
%{_bindir}/mf
%{_bindir}/mf-nowin
%{_mandir}/man1/inimf.1.*
%{_mandir}/man1/mf-nowin.1*
%{_mandir}/man1/mf.1*
%{_datadir}/texlive/texmf-dist/metafont/
%{_datadir}/texlive/fmtutil.cnf.d/metafont

%files -n texlive-metapost
%license lgpl2.1.txt
%{_bindir}/dvitomp
%{_bindir}/mfplain
%{_bindir}/mpost
%{_mandir}/man1/dvitomp.1*
%{_mandir}/man1/mpost.1*
%{_datadir}/texlive/texmf-dist/fonts/afm/metapost/
%{_datadir}/texlive/texmf-dist/fonts/enc/dvips/metapost/
%{_datadir}/texlive/texmf-dist/fonts/map/dvips/metapost/
%{_datadir}/texlive/texmf-dist/fonts/tfm/metapost/
%{_datadir}/texlive/texmf-dist/fonts/type1/metapost/
%{_datadir}/texlive/texmf-dist/metapost/
%{_datadir}/texlive/texmf-dist/tex/generic/metapost/
%doc %{_datadir}/texlive/texmf-dist/doc/metapost/

%files -n texlive-mex
%license pd.txt
%{_bindir}/mex
%{_bindir}/pdfmex
%{_bindir}/utf8mex
%{_datadir}/texlive/texmf-dist/tex/mex/
%{_datadir}/texlive/fmtutil.cnf.d/mex
%doc %{_datadir}/texlive/texmf-dist/doc/mex/

%files -n texlive-mflua
%license gpl2.txt
%{_bindir}/mflua
%{_bindir}/mflua-nowin
%ifnarch aarch64 loongarch64
%{_bindir}/mfluajit
%{_bindir}/mfluajit-nowin
%endif
%{_datadir}/texlive/fmtutil.cnf.d/mflua
%{_datadir}/texlive/texmf-dist/scripts/mflua/

%files -n texlive-mfware
%license knuth.txt
%{_bindir}/gftodvi
%{_bindir}/gftopk
%{_bindir}/gftype
%{_bindir}/mft
%{_bindir}/pktogf
%{_bindir}/pktype
%{_mandir}/man1/gftodvi.1*
%{_mandir}/man1/gftopk.1*
%{_mandir}/man1/gftype.1*
%{_mandir}/man1/mft.1*
%{_mandir}/man1/pktogf.1*
%{_mandir}/man1/pktype.1*
%{_datadir}/texlive/texmf-dist/mft/

%files -n texlive-mf2pt1
%license lppl1.txt
%{_bindir}/mf2pt1
%{_infodir}/mf2pt1.info*
%{_datadir}/texlive/texmf-dist/metapost/mf2pt1/
%{_datadir}/texlive/texmf-dist/scripts/mf2pt1/
%doc %{_datadir}/texlive/texmf-dist/doc/support/mf2pt1/

%files -n texlive-mkgrkindex
%{_bindir}/mkgrkindex
%{_datadir}/texlive/texmf-dist/makeindex/mkgrkindex/
%{_datadir}/texlive/texmf-dist/scripts/mkgrkindex/
%doc %{_datadir}/texlive/texmf-dist/doc/support/mkgrkindex/

%files -n texlive-mkjobtexmf
%{_bindir}/mkjobtexmf
%{_mandir}/man1/mkjobtexmf.1*
%{_datadir}/texlive/texmf-dist/scripts/mkjobtexmf/
%doc %{_datadir}/texlive/texmf-dist/doc/generic/mkjobtexmf/

%files -n texlive-mkpic
%license gpl.txt
%{_bindir}/mkpic
%{_datadir}/texlive/texmf-dist/scripts/mkpic/
%doc %{_datadir}/texlive/texmf-dist/doc/support/mkpic/

%files -n texlive-mltex
%license knuth.txt
%{_bindir}/mllatex
%{_bindir}/mltex
%{_datadir}/texlive/texmf-dist/tex/latex/mltex/
%{_datadir}/texlive/texmf-dist/tex/mltex/
%{_datadir}/texlive/fmtutil.cnf.d/mltex
%doc %{_datadir}/texlive/texmf-dist/doc/latex/mltex/

%files -n texlive-mptopdf
%license lppl1.txt
%{_bindir}/mptopdf
%{_mandir}/man1/mptopdf.1*
%{_datadir}/texlive/texmf-dist/scripts/context/perl/mptopdf.pl
%{_datadir}/texlive/texmf-dist/tex/context/base/mkii/supp-mis.mkii
%{_datadir}/texlive/texmf-dist/tex/context/base/mkii/supp-mpe.mkii
%{_datadir}/texlive/texmf-dist/tex/context/base/mkii/supp-pdf.mkii
%{_datadir}/texlive/texmf-dist/tex/context/base/mkii/syst-tex.mkii
%{_datadir}/texlive/texmf-dist/tex/generic/context/mptopdf/
%{_datadir}/texlive/fmtutil.cnf.d/mptopdf
%doc %{_datadir}/texlive/texmf-dist/doc/context/scripts/mkii/mptopdf.man

%files -n texlive-multibibliography
%license lppl1.3.txt
%{_bindir}/multibibliography
%{_datadir}/texlive/texmf-dist/bibtex/bst/multibibliography/
%{_datadir}/texlive/texmf-dist/scripts/multibibliography/
%{_datadir}/texlive/texmf-dist/tex/latex/multibibliography/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/multibibliography/

%files -n texlive-musixtex
%license gpl2.txt
%{_bindir}/musixflx
%{_bindir}/musixtex
%{_mandir}/man1/musixflx.1*
%{_mandir}/man1/musixtex.1*
%{_datadir}/texlive/texmf-dist/dvips/musixtex/
%{_datadir}/texlive/texmf-dist/scripts/musixtex/
%{_datadir}/texlive/texmf-dist/tex/generic/musixtex/
%{_datadir}/texlive/texmf-dist/tex/latex/musixtex/
%doc %{_datadir}/texlive/texmf-dist/doc/generic/musixtex/

%files -n texlive-musixtnt
%license gpl2.txt
%{_bindir}/msxlint
%{_mandir}/man1/msxlint.1*
%{_datadir}/texlive/texmf-dist/tex/generic/musixtnt/
%doc %{_datadir}/texlive/texmf-dist/doc/generic/musixtnt/

%files -n texlive-m-tx
%license gpl.txt
%{_bindir}/m-tx
%{_bindir}/prepmx
%{_mandir}/man1/prepmx.1*
%{_datadir}/texlive/texmf-dist/scripts/m-tx/
%{_datadir}/texlive/texmf-dist/tex/generic/m-tx/
%doc %{_datadir}/texlive/texmf-dist/doc/generic/m-tx/

%files -n texlive-oberdiek
%license lppl1.txt
%{_datadir}/texlive/texmf-dist/bibtex/bib/oberdiek/
%{_datadir}/texlive/texmf-dist/scripts/oberdiek/
%{_datadir}/texlive/texmf-dist/tex/generic/oberdiek/
%{_datadir}/texlive/texmf-dist/tex/latex/oberdiek/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/oberdiek/

%files -n texlive-omegaware
%license lppl1.txt
%{_bindir}/odvicopy
%{_bindir}/odvitype
%{_bindir}/ofm2opl
%{_bindir}/omfonts
%{_bindir}/opl2ofm
%{_bindir}/otangle
%{_bindir}/otp2ocp
%{_bindir}/outocp
%{_bindir}/ovf2ovp
%{_bindir}/ovp2ovf
%{_bindir}/wofm2opl
%{_bindir}/wopl2ofm
%{_bindir}/wovf2ovp
%{_mandir}/man1/odvicopy.1*
%{_mandir}/man1/odvitype.1*
%{_mandir}/man1/ofm2opl.1*
%{_mandir}/man1/opl2ofm.1*
%{_mandir}/man1/otangle.1*
%{_mandir}/man1/otp2ocp.1*
%{_mandir}/man1/outocp.1*
%{_mandir}/man1/ovf2ovp.1*
%{_mandir}/man1/ovp2ovf.1*

%files -n texlive-patgen
%license knuth.txt
%{_bindir}/patgen
%{_mandir}/man1/patgen.1*

%files -n texlive-pax
%{_bindir}/pdfannotextractor
%{_datadir}/texlive/texmf-dist/scripts/pax/
%{_datadir}/texlive/texmf-dist/tex/latex/pax/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/pax/

%files -n texlive-pdfbook2
%license gpl3.txt
%{_bindir}/pdfbook2
%{_mandir}/man1/pdfbook2.1*
%{_datadir}/texlive/texmf-dist/scripts/pdfbook2/
%doc %{_datadir}/texlive/texmf-dist/doc/support/pdfbook2/

%files -n texlive-pdfcrop
%license lppl1.txt
%{_bindir}/pdfcrop
%{_bindir}/rpdfcrop
%{_datadir}/texlive/texmf-dist/scripts/pdfcrop/
%doc %{_datadir}/texlive/texmf-dist/doc/support/pdfcrop/

%files -n texlive-pdfjam
%license gpl2.txt
%{_bindir}/pdf180
%{_bindir}/pdf270
%{_bindir}/pdf90
%{_bindir}/pdfbook
%{_bindir}/pdfflip
%{_bindir}/pdfjam
%{_bindir}/pdfjam-pocketmod
%{_bindir}/pdfjam-slides3up
%{_bindir}/pdfjam-slides6up
%{_bindir}/pdfjoin
%{_bindir}/pdfnup
%{_bindir}/pdfpun
%{_mandir}/man1/pdf180.1*
%{_mandir}/man1/pdf270.1*
%{_mandir}/man1/pdf90.1*
%{_mandir}/man1/pdfbook.1*
%{_mandir}/man1/pdfflip.1*
%{_mandir}/man1/pdfjam-pocketmod.1*
%{_mandir}/man1/pdfjam-slides3up.1*
%{_mandir}/man1/pdfjam-slides6up.1*
%{_mandir}/man1/pdfjam.1*
%{_mandir}/man1/pdfjoin.1*
%{_mandir}/man1/pdfnup.1*
%{_mandir}/man1/pdfpun.1*
%{_datadir}/texlive/texmf-dist/scripts/pdfjam/
%doc %{_datadir}/texlive/texmf-dist/doc/support/pdfjam/

%files -n texlive-pdflatexpicscale
%license lppl.txt
%{_bindir}/pdflatexpicscale
%{_datadir}/texlive/texmf-dist/scripts/pdflatexpicscale
%doc %{_datadir}/texlive/texmf-dist/doc/support/pdflatexpicscale

%files -n texlive-pdftex
%license gpl.txt
%{_bindir}/etex
%{_bindir}/pdfetex
%{_bindir}/pdftex
%{_bindir}/simpdftex
%{_mandir}/man1/pdfetex.1*
%{_mandir}/man1/pdftex.1*
%{_datadir}/texlive/texmf-dist/fonts/map/dvips/dummy-space/dummy-space.map
%{_datadir}/texlive/texmf-dist/fonts/tfm/public/pdftex/
%{_datadir}/texlive/texmf-dist/fonts/type1/public/pdftex/
%{_datadir}/texlive/texmf-dist/scripts/simpdftex/simpdftex
%{_datadir}/texlive/texmf-dist/tex/generic/config/pdftex-dvi.tex
%{_datadir}/texlive/texmf-dist/tex/generic/pdftex/
%{_datadir}/texlive/fmtutil.cnf.d/pdftex
%doc %{_datadir}/texlive/texmf-dist/doc/pdftex/

%files -n texlive-pdftools
%license pd.txt
%{_bindir}/e2pall
%{_bindir}/pdfatfi
%{_bindir}/pdfclose
%{_bindir}/pdfopen
%{_bindir}/pdftosrc
%{_mandir}/man1/e2pall.1*
%{_mandir}/man1/pdfclose.1*
%{_mandir}/man1/pdfopen.1*
%{_mandir}/man1/pdftosrc.1*
%{_datadir}/texlive/texmf-dist/scripts/texlive/e2pall.pl

%files -n texlive-pdfxup
%license lppl1.3.txt
%{_bindir}/pdfxup
%{_mandir}/man1/pdfxup.1*
%{_datadir}/texlive/texmf-dist/scripts/pdfxup/
%doc %{_datadir}/texlive/texmf-dist/doc/support/pdfxup/

%files -n texlive-pedigree-perl
%license gpl2.txt
%{_bindir}/pedigree
%{_mandir}/man1/pedigree.1*
%{_datadir}/texlive/texmf-dist/scripts/pedigree-perl/
%doc %{_datadir}/texlive/texmf-dist/doc/support/pedigree-perl/

%files -n texlive-perltex
%license lppl1.txt
%{_bindir}/perltex
%{_mandir}/man1/perltex.1*
%{_datadir}/texlive/texmf-dist/scripts/perltex/
%{_datadir}/texlive/texmf-dist/tex/latex/perltex/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/perltex/

%files -n texlive-petri-nets
%license gpl.txt
%{_bindir}/pn2pdf
%{_datadir}/texlive/texmf-dist/scripts/petri-nets/
%{_datadir}/texlive/texmf-dist/tex/generic/petri-nets/
%doc %{_datadir}/texlive/texmf-dist/doc/generic/petri-nets/

%files -n texlive-pfarrei
%license lppl1.3.txt
%{_bindir}/a5toa4
%{_bindir}/pfarrei
%{_datadir}/texlive/texmf-dist/scripts/pfarrei/
%{_datadir}/texlive/texmf-dist/tex/latex/pfarrei/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/pfarrei/

%files -n texlive-pkfix
%license lppl1.3.txt
%{_bindir}/pkfix
%{_datadir}/texlive/texmf-dist/scripts/pkfix/
%doc %{_datadir}/texlive/texmf-dist/doc/support/pkfix/

%files -n texlive-pkfix-helper
%license lppl1.txt
%{_bindir}/pkfix-helper
%{_mandir}/man1/pkfix-helper.1*
%{_datadir}/texlive/texmf-dist/scripts/pkfix-helper/
%doc %{_datadir}/texlive/texmf-dist/doc/support/pkfix-helper/

%files -n texlive-pmx
%license gpl2.txt
%{_bindir}/pmxab
%{_bindir}/scor2prt
%{_mandir}/man1/pmxab.1*
%{_mandir}/man1/scor2prt.1*
%{_datadir}/texlive/texmf-dist/tex/generic/pmx/
%{_datadir}/texlive/texmf-dist/scripts/pmx/
%doc %{_datadir}/texlive/texmf-dist/doc/generic/pmx/

%files -n texlive-pmxchords
%license gpl2.txt
%{_bindir}/pmxchords
%{_mandir}/man1/pmxchords.1*
%{_datadir}/texlive/texmf-dist/scripts/pmxchords/
%{_datadir}/texlive/texmf-dist/tex/generic/pmxchords/
%doc %{_datadir}/texlive/texmf-dist/doc/pmxchords/

%files -n texlive-pstools
%license gpl.txt
%{_bindir}/bbox
%{_bindir}/ps2eps
%{_bindir}/ps2frag
%{_bindir}/pslatex
%{_mandir}/man1/bbox.1*
%{_mandir}/man1/ps2eps.1*
%{_mandir}/man1/ps2frag.1*
%{_mandir}/man1/pslatex.1*
%{_datadir}/texlive/texmf-dist/scripts/texlive/ps2frag.sh
%{_datadir}/texlive/texmf-dist/scripts/texlive/pslatex.sh
%{_datadir}/texlive/texmf-dist/scripts/ps2eps/

%files -n texlive-pst2pdf
%license gpl2.txt
%{_bindir}/pst2pdf
%{_datadir}/texlive/texmf-dist/scripts/pst2pdf/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/pst2pdf/

%files -n texlive-pst-pdf
%license lppl1.txt
%{_bindir}/ps4pdf
%{_datadir}/texlive/texmf-dist/scripts/pst-pdf/
%{_datadir}/texlive/texmf-dist/tex/latex/pst-pdf/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/pst-pdf/

%files -n texlive-ps2pk
%license other-free.txt
%{_bindir}/mag
%{_bindir}/pfb2pfa
%{_bindir}/pk2bm
%{_bindir}/ps2pk
%{_mandir}/man1/mag.1*
%{_mandir}/man1/pfb2pfa.1*
%{_mandir}/man1/pk2bm.1*
%{_mandir}/man1/ps2pk.1*

%files -n texlive-ptex
%{_bindir}/eptex
%{_bindir}/makejvf
%{_bindir}/mendex
%{_bindir}/pbibtex
%{_bindir}/pdvitomp
%{_bindir}/pdvitype
%{_bindir}/platex
%{_bindir}/pmpost
%{_bindir}/ppltotf
%{_bindir}/ptex
%{_bindir}/ptftopl
%{_mandir}/man1/eptex.1*
%{_mandir}/man1/makejvf.1*
%{_mandir}/man1/mendex.1*
%{_mandir}/man1/ptex.1*
%{_datadir}/texlive/fmtutil.cnf.d/platex
%{_datadir}/texlive/fmtutil.cnf.d/ptex

%files -n texlive-ptex-fontmaps
%license gpl3.txt
%license pd.txt
%{_bindir}/kanji-config-updmap
%{_bindir}/kanji-config-updmap-sys
%{_bindir}/kanji-config-updmap-user
%{_bindir}/kanji-fontmap-creator
%{_datadir}/texlive/texmf-dist/fonts/cmap/ptex-fontmaps
%{_datadir}/texlive/texmf-dist/fonts/map/dvipdfmx/ptex-fontmaps
%{_datadir}/texlive/texmf-dist/fonts/misc/ptex-fontmaps/
%{_datadir}/texlive/texmf-dist/scripts/ptex-fontmaps
%doc %{_datadir}/texlive/texmf-dist/doc/fonts/ptex-fontmaps

%files -n texlive-ptex2pdf
%license gpl2.txt
%{_bindir}/ptex2pdf
%{_datadir}/texlive/texmf-dist/scripts/ptex2pdf/
%{_datadir}/texlive/tlpkg/tlpostcode/ptex2pdf-tlpost.pl
%doc %{_datadir}/texlive/texmf-dist/doc/latex/ptex2pdf/

%files -n texlive-purifyeps
%license lppl1.txt
%{_bindir}/purifyeps
%{_mandir}/man1/purifyeps.1*
%{_datadir}/texlive/texmf-dist/scripts/purifyeps/
%doc %{_datadir}/texlive/texmf-dist/doc/support/purifyeps/

%files -n texlive-pygmentex
%license lppl1.3.txt
%{_bindir}/pygmentex
%{_datadir}/texlive/texmf-dist/scripts/pygmentex/
%{_datadir}/texlive/texmf-dist/tex/latex/pygmentex/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/pygmentex/

%files -n texlive-pythontex
%license lppl1.3.txt
%{_bindir}/depythontex
%{_bindir}/pythontex
%{_datadir}/texlive/texmf-dist/scripts/pythontex/
%{_datadir}/texlive/texmf-dist/tex/latex/pythontex/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/pythontex/

%files -n texlive-rubik
%license lppl1.3.txt
%{_bindir}/rubikrotation
%{_mandir}/man1/rubikrotation.1*
%{_datadir}/texlive/texmf-dist/scripts/rubik/
%{_datadir}/texlive/texmf-dist/tex/latex/rubik/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/rubik/

%files -n texlive-seetexk
%{_bindir}/dvibook
%{_bindir}/dviconcat
%{_bindir}/dviselect
%{_bindir}/dvitodvi
%{_mandir}/man1/dvibook.1*
%{_mandir}/man1/dviconcat.1*
%{_mandir}/man1/dviselect.1*
%{_mandir}/man1/dvitodvi.1*

%files -n texlive-splitindex
%license lppl1.txt
%{_bindir}/splitindex
%{_mandir}/man1/splitindex.1*
%{_datadir}/texlive/texmf-dist/scripts/splitindex/
%{_datadir}/texlive/texmf-dist/tex/generic/splitindex/
%{_datadir}/texlive/texmf-dist/tex/latex/splitindex/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/splitindex/

%files -n texlive-srcredact
%license gpl2.txt
%{_bindir}/srcredact
%{_mandir}/man1/srcredact.1*
%{_datadir}/texlive/texmf-dist/scripts/srcredact/
%doc %{_datadir}/texlive/texmf-dist/doc/support/srcredact/

%files -n texlive-sty2dtx
%license gpl3.txt
%{_bindir}/sty2dtx
%{_mandir}/man1/sty2dtx.1*
%{_datadir}/texlive/texmf-dist/scripts/sty2dtx/
%doc %{_datadir}/texlive/texmf-dist/doc/support/sty2dtx/

%files -n texlive-svn-multi
%license lppl1.txt
%{_bindir}/svn-multi
%{_datadir}/texlive/texmf-dist/scripts/svn-multi/
%{_datadir}/texlive/texmf-dist/tex/latex/svn-multi/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/svn-multi/
%doc %{_datadir}/texlive/texmf-dist/doc/support/svn-multi/

%files -n texlive-synctex
%license lppl1.txt
%{_bindir}/synctex
%{_mandir}/man1/synctex.1*
%{_mandir}/man5/synctex.5*

%files -n texlive-tetex
%{_bindir}/allcm
%{_bindir}/allec
%{_bindir}/allneeded
%{_bindir}/dvi2fax
%{_bindir}/dvired
%{_bindir}/fmtutil
%{_bindir}/fmtutil-sys
%{_bindir}/fmtutil-user
%{_bindir}/kpsepath
%{_bindir}/kpsetool
%{_bindir}/kpsewhere
%{_bindir}/kpsexpand
%{_bindir}/texconfig-dialog
%{_bindir}/texconfig-sys
%{_bindir}/texlinks
%{_bindir}/updmap
%{_bindir}/updmap-sys
%{_bindir}/updmap-user
%{_mandir}/man1/allcm.1*
%{_mandir}/man1/allec.1*
%{_mandir}/man1/allneeded.1*
%{_mandir}/man1/dvi2fax.1*
%{_mandir}/man1/dvired.1*
%{_mandir}/man1/fmtutil-sys.1*
%{_mandir}/man1/fmtutil-user.1*
%{_mandir}/man1/fmtutil.1*
%{_mandir}/man1/kpsepath.1*
%{_mandir}/man1/kpsetool.1*
%{_mandir}/man1/kpsewhere.1*
%{_mandir}/man1/kpsexpand.1*
%{_mandir}/man1/texlinks.1*
%{_mandir}/man1/updmap-sys.1*
%{_mandir}/man1/updmap-user.1*
%{_mandir}/man1/updmap.1*
%{_datadir}/texlive/texmf-dist/scripts/texlive/allcm.sh
%{_datadir}/texlive/texmf-dist/scripts/texlive/allneeded.sh
%{_datadir}/texlive/texmf-dist/scripts/texlive/dvi2fax.sh
%{_datadir}/texlive/texmf-dist/scripts/texlive/dvired.sh
%{_datadir}/texlive/texmf-dist/scripts/texlive/fmtutil-sys.sh
%{_datadir}/texlive/texmf-dist/scripts/texlive/fmtutil-user.sh
%{_datadir}/texlive/texmf-dist/scripts/texlive/fmtutil.pl
%{_datadir}/texlive/texmf-dist/scripts/texlive/kpsetool.sh
%{_datadir}/texlive/texmf-dist/scripts/texlive/kpsewhere.sh
%{_datadir}/texlive/texmf-dist/scripts/texlive/mktexlsr.pl
%{_datadir}/texlive/texmf-dist/scripts/texlive/texconfig-dialog.sh
%{_datadir}/texlive/texmf-dist/scripts/texlive/texconfig-sys.sh
%{_datadir}/texlive/texmf-dist/scripts/texlive/texlinks.sh
%{_datadir}/texlive/texmf-dist/scripts/texlive/updmap-sys.sh
%{_datadir}/texlive/texmf-dist/scripts/texlive/updmap-user.sh
%{_datadir}/texlive/texmf-dist/scripts/texlive/updmap.pl
%config(noreplace) %{_sysconfdir}/texlive/web2c/updmap.cfg
%{_datadir}/texlive/texmf-dist/web2c/updmap.cfg
%{_mandir}/man5/fmtutil.cnf.5*
%{_mandir}/man5/updmap.cfg.5*
%{_datadir}/texlive/texmf-dist/dvips/tetex/
%{_datadir}/texlive/texmf-dist/fonts/enc/dvips/tetex/
%{_datadir}/texlive/texmf-dist/fonts/map/dvips/tetex/
%doc %{_datadir}/texlive/texmf-dist/doc/tetex/

%files -n texlive-tex
%license knuth.txt
%{_bindir}/initex
%{_bindir}/tex
%{_mandir}/man1/initex.1*
%{_mandir}/man1/tex.1*
%{_datadir}/texlive/fmtutil.cnf.d/tex

%files -n texlive-tex4ebook
%license lppl1.3.txt
%{_bindir}/tex4ebook
%{_datadir}/texlive/texmf-dist/scripts/tex4ebook/
%{_datadir}/texlive/texmf-dist/tex/latex/tex4ebook/
%doc %{_datadir}/texlive/texmf-dist/doc/support/tex4ebook/

%files -n texlive-tex4ht
%license lppl1.txt
%{_bindir}/ht
%{_bindir}/htcontext
%{_bindir}/htlatex
%{_bindir}/htmex
%{_bindir}/httex
%{_bindir}/httexi
%{_bindir}/htxelatex
%{_bindir}/htxetex
%{_bindir}/mk4ht
%{_bindir}/t4ht
%{_bindir}/tex4ht
%{_bindir}/xhlatex
%{_datadir}/texlive/texmf-dist/scripts/tex4ht/
%{_datadir}/texlive/texmf-dist/tex/generic/tex4ht/
%{_datadir}/texlive/texmf-dist/tex4ht/
%doc %{_datadir}/texlive/texmf-dist/doc/generic/tex4ht/

%files -n texlive-texconfig
%license lppl1.txt
%{_bindir}/texconfig
%{_mandir}/man1/texconfig-sys.1*
%{_mandir}/man1/texconfig.1*
%{_datadir}/texlive/texmf-dist/scripts/texlive/texconfig.sh
%{_datadir}/texlive/texmf-dist/texconfig/

%files -n texlive-texcount
%license lppl1.txt
%{_bindir}/texcount
%{_datadir}/texlive/texmf-dist/scripts/texcount/
%doc %{_datadir}/texlive/texmf-dist/doc/support/texcount/

%files -n texlive-texdef
%license gpl3.txt
%{_bindir}/latexdef
%{_bindir}/texdef
%{_datadir}/texlive/texmf-dist/scripts/texdef/
%doc %{_datadir}/texlive/texmf-dist/doc/support/texdef/

%files -n texlive-texdiff
%license gpl.txt
%{_bindir}/texdiff
%{_datadir}/texlive/texmf-dist/scripts/texdiff
%{_mandir}/man1/texdiff.1*
%doc %{_datadir}/texlive/texmf-dist/doc/support/texdiff/

%files -n texlive-texdirflatten
%{_bindir}/texdirflatten
%{_mandir}/man1/texdirflatten.1*
%{_datadir}/texlive/texmf-dist/scripts/texdirflatten/
%doc %{_datadir}/texlive/texmf-dist/doc/support/texdirflatten/

%files -n texlive-texdoc
%license gpl.txt
%{_bindir}/texdoc
%{_mandir}/man1/texdoc.1*
%{_datadir}/texlive/texmf-dist/scripts/texdoc/
%{_datadir}/texlive/texmf-dist/texdoc/
%doc %{_datadir}/texlive/texmf-dist/doc/support/texdoc/

%files -n texlive-texdoctk
%license gpl.txt
%{_bindir}/texdoctk
%{_mandir}/man1/texdoctk.1*
%{_datadir}/texlive/texmf-dist/scripts/texdoctk/
%{_datadir}/texlive/texmf-dist/texdoctk/

%files -n texlive-texfot
%license pd.txt
%{_bindir}/texfot
%{_mandir}/man1/texfot.1*
%{_datadir}/texlive/texmf-dist/scripts/texfot/
%doc %{_datadir}/texlive/texmf-dist/doc/support/texfot/

%files -n texlive-texliveonfly
%license gpl3.txt
%{_bindir}/texliveonfly
%{_datadir}/texlive/texmf-dist/scripts/texliveonfly/
%doc %{_datadir}/texlive/texmf-dist/doc/support/texliveonfly/

%files -n texlive-texlive-en
%{_infodir}/tlbuild.info*
%doc %{_datadir}/texlive/texmf-dist/doc/texlive/texlive-en/
%doc %{_datadir}/texlive/texmf-dist/doc/texlive/tlbuild/tlbuild.html
%doc %{_datadir}/texlive/texmf-dist/doc/texlive/tlbuild/tlbuild.pdf

%files -n texlive-texlive-scripts
%license lppl1.txt
%{_bindir}/rungs
%{_mandir}/man1/install-tl.1*
%{_datadir}/texlive/texmf-dist/scripts/texlive/rungs.tlu
%{_datadir}/texlive/texmf-dist/scripts/texlive/test-tlpdb.tlu
%{_datadir}/texlive/texmf-dist/scripts/texlive/texconf.tlu
%{_datadir}/texlive/texmf-dist/scripts/texlive/lua/texlive/getopt.tlu
%{_datadir}/texlive/texmf-dist/scripts/texlive/lua/texlive/tlpdb.tlu
%{_datadir}/texlive/texmf-dist/scripts/texlive/lua/texlive/utils.tlu

%files -n texlive-texlive.infra
%license lppl1.txt
%{_datadir}/texlive/texmf-dist/web2c/fmtutil-hdr.cnf
%{_datadir}/texlive/texmf-dist/web2c/updmap-hdr.cfg
%{_datadir}/texlive/LICENSE.CTAN
%{_datadir}/texlive/LICENSE.TL
%{_datadir}/texlive/README
%{_datadir}/texlive/README.usergroups
%{_datadir}/texlive/index.html
%{_datadir}/texlive/readme-html.dir/readme.cs.html
%{_datadir}/texlive/readme-html.dir/readme.de.html
%{_datadir}/texlive/readme-html.dir/readme.en.html
%{_datadir}/texlive/readme-html.dir/readme.es.html
%{_datadir}/texlive/readme-html.dir/readme.fr.html
%{_datadir}/texlive/readme-html.dir/readme.it.html
%{_datadir}/texlive/readme-html.dir/readme.ja.html
%{_datadir}/texlive/readme-html.dir/readme.pl.html
%{_datadir}/texlive/readme-html.dir/readme.pt-br.html
%{_datadir}/texlive/readme-html.dir/readme.ru.html
%{_datadir}/texlive/readme-html.dir/readme.sr.html
%{_datadir}/texlive/readme-html.dir/readme.zh-cn.html
%{_datadir}/texlive/release-texlive.txt
%{_datadir}/texlive/tlpkg/TeXLive/TLConfFile.pm
%{_datadir}/texlive/tlpkg/TeXLive/TLConfig.pm
%{_datadir}/texlive/tlpkg/TeXLive/TLCrypto.pm
%{_datadir}/texlive/tlpkg/TeXLive/TLDownload.pm
%{_datadir}/texlive/tlpkg/TeXLive/TLPDB.pm
%{_datadir}/texlive/tlpkg/TeXLive/TLPOBJ.pm
%{_datadir}/texlive/tlpkg/TeXLive/TLPSRC.pm
%{_datadir}/texlive/tlpkg/TeXLive/TLPaper.pm
%{_datadir}/texlive/tlpkg/TeXLive/TLTREE.pm
%{_datadir}/texlive/tlpkg/TeXLive/TLUtils.pm
%{_datadir}/texlive/tlpkg/TeXLive/TLWinGoo.pm
%{_datadir}/texlive/tlpkg/TeXLive/TeXCatalogue.pm
%{_datadir}/texlive/tlpkg/TeXLive/trans.pl
%doc %{_datadir}/texlive/texmf-dist/scripts/texlive/NEWS
%doc %{_datadir}/texlive/tlpkg/README

%files -n texlive-texloganalyser
%{_bindir}/texloganalyser
%{_datadir}/texlive/texmf-dist/scripts/texloganalyser/
%doc %{_datadir}/texlive/texmf-dist/doc/support/texloganalyser/

%files -n texlive-texosquery
%license lppl1.3.txt
%{_bindir}/texosquery*
%{_datadir}/texlive/texmf-dist/scripts/texosquery
%{_datadir}/texlive/texmf-dist/tex/latex/texosquery
%doc %{_datadir}/texlive/texmf-dist/doc/support/texosquery

%files -n texlive-texsis
%license lppl1.txt
%{_bindir}/texsis
%{_mandir}/man1/texsis.1*
%{_datadir}/texlive/texmf-dist/bibtex/bst/texsis/
%{_datadir}/texlive/texmf-dist/tex/texsis/
%{_datadir}/texlive/fmtutil.cnf.d/texsis
%doc %{_datadir}/texlive/texmf-dist/doc/otherformats/texsis/

%files -n texlive-texware
%license knuth.txt
%{_bindir}/dvitype
%{_bindir}/pooltype
%{_mandir}/man1/dvitype.1*
%{_mandir}/man1/pooltype.1*

%files -n texlive-thumbpdf
%license lppl1.txt
%{_bindir}/thumbpdf
%{_mandir}/man1/thumbpdf.1*
%{_datadir}/texlive/texmf-dist/scripts/thumbpdf/
%{_datadir}/texlive/texmf-dist/tex/generic/thumbpdf/
%doc %{_datadir}/texlive/texmf-dist/doc/generic/thumbpdf/

%files -n texlive-tie
%{_bindir}/tie
%{_mandir}/man1/tie.1*

%files -n texlive-tpic2pdftex
%license gpl.txt
%{_bindir}/tpic2pdftex
%{_mandir}/man1/tpic2pdftex.1*
%doc %{_datadir}/texlive/texmf-dist/doc/tpic2pdftex/

%files -n texlive-ttfutils
%license lppl1.txt
%{_bindir}/ttf2afm
%{_bindir}/ttf2pk
%{_bindir}/ttf2tfm
%{_bindir}/ttfdump
%{_mandir}/man1/ttf2afm.1*
%{_mandir}/man1/ttf2pk.1*
%{_mandir}/man1/ttf2tfm.1*
%{_mandir}/man1/ttfdump.1*
%{_datadir}/texlive/texmf-dist/fonts/enc/ttf2pk/
%{_datadir}/texlive/texmf-dist/fonts/sfd/ttf2pk/
%{_datadir}/texlive/texmf-dist/ttf2pk/
%doc %{_datadir}/texlive/texmf-dist/doc/ttf2pk/

%files -n texlive-typeoutfileinfo
%license lppl1.3.txt
%{_bindir}/typeoutfileinfo
%{_datadir}/texlive/texmf-dist/scripts/typeoutfileinfo/
%doc %{_datadir}/texlive/texmf-dist/doc/support/typeoutfileinfo/

%files -n texlive-ulqda
%license lppl1.txt
%{_bindir}/ulqda
%{_datadir}/texlive/texmf-dist/scripts/ulqda/
%{_datadir}/texlive/texmf-dist/tex/latex/ulqda/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/ulqda/

%files -n texlive-uptex
%{_bindir}/euptex
%{_bindir}/upbibtex
%{_bindir}/updvitomp
%{_bindir}/updvitype
%{_bindir}/uplatex
%{_bindir}/upmendex
%{_bindir}/upmpost
%{_bindir}/uppltotf
%{_bindir}/uptex
%{_bindir}/uptftopl
%{_bindir}/wovp2ovf
%{_mandir}/man1/euptex.1*
%{_mandir}/man1/uplatex.1*
%{_mandir}/man1/uptex.1*
%{_datadir}/texlive/fmtutil.cnf.d/uplatex
%{_datadir}/texlive/fmtutil.cnf.d/uptex
%doc %{_datadir}/texlive/texmf-dist/doc/upmendex/
%doc %{_datadir}/texlive/texmf-dist/doc/uplatex/

%files -n texlive-urlbst
%license gpl.txt
%{_bindir}/urlbst
%{_datadir}/texlive/texmf-dist/bibtex/bst/urlbst/
%{_datadir}/texlive/texmf-dist/scripts/urlbst/
%doc %{_datadir}/texlive/texmf-dist/doc/bibtex/urlbst/

%files -n texlive-velthuis
%license gpl.txt
%{_bindir}/devnag
%{_mandir}/man1/devnag.1*
%{_datadir}/texlive/texmf-dist/fonts/afm/public/velthuis/
%{_datadir}/texlive/texmf-dist/fonts/map/dvips/velthuis/
%{_datadir}/texlive/texmf-dist/fonts/source/public/velthuis/
%{_datadir}/texlive/texmf-dist/fonts/tfm/public/velthuis/
%{_datadir}/texlive/texmf-dist/fonts/type1/public/velthuis/
%{_datadir}/texlive/texmf-dist/tex/generic/velthuis/
%{_datadir}/texlive/texmf-dist/tex/latex/velthuis/
%{_datadir}/texlive/texmf-dist/tex/plain/velthuis/
%{_datadir}/texlive/texmf-dist/tex/xelatex/velthuis/
%doc %{_datadir}/texlive/texmf-dist/doc/generic/velthuis/

%files -n texlive-vlna
%license lppl1.txt
%{_bindir}/vlna
%{_mandir}/man1/vlna.1*
%doc %{_datadir}/texlive/texmf-dist/doc/vlna/

%files -n texlive-vpe
%license lppl1.txt
%{_bindir}/vpe
%{_datadir}/texlive/texmf-dist/scripts/vpe/
%{_datadir}/texlive/texmf-dist/tex/latex/vpe/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/vpe/

%files -n texlive-web
%license knuth.txt
%{_bindir}/tangle
%{_bindir}/weave
%{_mandir}/man1/tangle.1*
%{_mandir}/man1/weave.1*

%files -n texlive-wordcount
%license lppl1.txt
%{_bindir}/wordcount
%{_datadir}/texlive/texmf-dist/scripts/wordcount/
%{_datadir}/texlive/texmf-dist/tex/latex/wordcount/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/wordcount/

%files -n texlive-xdvi
%{_bindir}/xdvi
%{_bindir}/xdvi-xaw
%{_mandir}/man1/xdvi.1*
%{_datadir}/texlive/texmf-dist/dvips/xdvi/
%{_datadir}/texlive/texmf-dist/xdvi/

%files -n texlive-xetex
%license other-free.txt
%{_bindir}/xdvipdfmx
%{_bindir}/xelatex
%{_bindir}/xetex
%{_mandir}/man1/xelatex.1*
%{_datadir}/texlive/tlpkg/tlpostcode/xetex.pl
%{_datadir}/texlive/texmf-dist/fonts/misc/xetex/
%{_datadir}/texlive/fmtutil.cnf.d/xetex
%doc %{_datadir}/texlive/texmf-dist/doc/xetex/

%ifarch empty
%files -n texlive-xindy
%license gpl.txt
%{_bindir}/tex2xindy
%{_bindir}/texindy
%{_bindir}/xindy
%{_bindir}/xindy.mem
%{_mandir}/man1/xindy.1*
%{_mandir}/man1/texindy.1*
%{_mandir}/man1/tex2xindy.1*
%{_datadir}/texlive/texmf-dist/scripts/xindy/
%{_datadir}/texlive/texmf-dist/xindy/
%doc %{_datadir}/texlive/texmf-dist/doc/xindy/
%endif

%files -n texlive-xmltex
%license lppl1.txt
%{_bindir}/pdfxmltex
%{_bindir}/xmltex
%{_datadir}/texlive/texmf-dist/tex/xmltex/
%{_datadir}/texlive/fmtutil.cnf.d/xmltex
%doc %{_datadir}/texlive/texmf-dist/doc/otherformats/xmltex/

%files -n texlive-yplan
%license lppl1.txt
%{_bindir}/yplan
%{_datadir}/texlive/texmf-dist/scripts/yplan/
%{_datadir}/texlive/texmf-dist/tex/latex/yplan/
%doc %{_datadir}/texlive/texmf-dist/doc/latex/yplan/

%changelog
* Wed Apr 20 2022 Ge Wang <wangge20@h-partners.com> - 20180414-34
- Add Loongarch architecture support

* Wed Jan 19 2022 xu_ping <xuping33@huawei.com> - 20180414-33
- remove useless BuildRequires poppler

* Wed Sep 10 2021 caodongxia <caodongxia@huawei.com> - 20180414-32
- Remove rpath

* Sat Jul 31 2021 Haiwei Li <lihaiwei8@huawei.com> - 20180414-31
- Fix compilation failed due to multiple definition

* Wed 30 Jun 2021 sunguoshuai <sunguoshuai@huawei.com> - 20180414-30
- Fix build error when srctopdf is ok

* Thu Sep 10 2020 baizhonggui <baizhonggui@huawei.com> - 20180414-29
- modify source0

* Mon Jan 20 2020 wutao <wutao@huawei.com> - 20180414-28
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Sun Jan 19 2020 wutao <wutao@huawei.com> - 20180414-27
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Wed Jan 15 2020 openEuler Buildteam <buildteam@openeuler.org> - 20180414-26
- remove useless BuildRequires.

* Thu Dec 12 2019 daiqianwen <daiqianwen@huawei.com> - 20180414-25
- Package init

