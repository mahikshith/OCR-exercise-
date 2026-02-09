Metrics :

Character Error Rate (CER)

CER measures the accuracy of the OCR at the character level. It is calculated by dividing the sum of character edits (substitutions, deletions, and insertions) by the total number of characters in the reference text.
CER=NS+D+I / N 

Where:

    S = Substitutions: Characters incorrectly identified (e.g., 'o' instead of 'a').

    D = Deletions: Characters missing from the OCR output.

    I = Insertions: Extra characters added by the OCR.

    N = Total Characters: The total number of characters in the original reference text.


Word Error Rate (WER)

WER measures the accuracy at the word level. While CER tells us how many letters were wrong, WER tells us how many words were completely or partially incorrect, which is often more representative of how readable the final text is.
WER=Nw​Sw​+Dw​+Iw​​

Where:

    Sw​ = Word Substitutions: Incorrect words.

    Dw​ = Word Deletions: Missing words.

    Iw​ = Word Insertions: Extra words.

    Nw​ = Total Words: The total number of words in the original reference text.

How they are interpreted:

    0.00 (0%): Represents a perfect match where the OCR output is identical to the human-transcribed ground truth.

    Lower Values: Indicate higher accuracy. In professional settings, a CER below 5% for handwriting is typically considered high quality.

    Higher Values: Suggest that the OCR struggled with the handwriting style, pen pressure, or image quality, resulting in many misreadings.



Metrics :


Image	Document Type	CER (%) [gemma]	WER (%) [gemma]	CER2 (%) [Qwen2.5-VL]	WER2 (%) [Qwen2.5-VL]	Status (Overall)
1	Antique Letter	0.08%	0.00%	2.15%	4.80%	Excellent
2	AI OCR Notes	0.14%	0.40%	1.80%	3.50%	Excellent
3	Notebook Page	0.31%	0.00%	2.45%	5.10%	Excellent
4	Journal Entry	0.30%	1.23%	3.20%	7.40%	Very High
