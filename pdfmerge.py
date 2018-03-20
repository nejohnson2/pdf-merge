'''
Adapted from Stackoverflow:
https://stackoverflow.com/questions/3444645/merge-pdf-files
'''
import sys, os, glob
from PyPDF2 import PdfFileMerger

def pdfMerge(dpath, output_path):
	'''Combine a group of pdfs into a single pdf
	Parameters
	----------
	dpath : string,
		Path the the folder where pdfs are located
	output_path : string,
		Output directory path
	'''
	# -- Get all .pdf files in the directory
	pdfs = glob.glob(os.path.join(dpath, '*.pdf'))

	# -- Use directory name as output file name
	fname = ''.join([os.path.split(dpath[:-1])[1], '.pdf'])

	# -- Build entire output path
	outFile = os.path.join(output_path, fname)
	
	# -- Merge pdfs
	merger = PdfFileMerger()

	for pdf in pdfs:
		merger.append(open(pdf, 'rb'))

	with open(outFile, 'wb') as fout:
		merger.write(fout)

def main(input_path, output_path):
	
	# -- get all folders that contain .pdfs
	for dpath in glob.glob(os.path.join(input_path, '*/')):

		# -- ignore the folder that ends with AUDIO
		if os.path.split(dpath[:-1])[1] != 'AUDIO':
			print '*' * 50
			pdfMerge(dpath, output_path)


if __name__ == '__main__':
	output_path = ''
	input_path = ''
	main(input_path, output_path)
