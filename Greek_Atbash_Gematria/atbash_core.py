#! sys/usr/env python3

import unicodedata

class GreekAtbashCipher:
	def __init__(self):
		# Greek alphabet and gematria (numerical values) without accented versions
		self.gematria = {
			'Α': 1, 'α': 1,
			'Β': 2, 'β': 2,
			'Γ': 3, 'γ': 3,
			'Δ': 4, 'δ': 4,
			'Ε': 5, 'ε': 5,
			'Ζ': 7, 'ζ': 7,
			'Η': 8, 'η': 8,
			'Θ': 9, 'θ': 9,
			'Ι': 10, 'ι': 10,
			'Κ': 20, 'κ': 20,
			'Λ': 30, 'λ': 30,
			'Μ': 40, 'μ': 40,
			'Ν': 50, 'ν': 50,
			'Ξ': 60, 'ξ': 60,
			'Ο': 70, 'ο': 70,
			'Π': 80, 'π': 80,
			'Ρ': 100, 'ρ': 100,
			'Σ': 200, 'σ': 200, 'ς': 200,
			'Τ': 300, 'τ': 300,
			'Υ': 400, 'υ': 400,
			'Φ': 500, 'φ': 500,
			'Χ': 600, 'χ': 600,
			'Ψ': 700, 'ψ': 700,
			'Ω': 800, 'ω': 800,
			# 'ϡ': 900
		}

		# Upper and lower Greek letters for mapping
		self.upper = [k for k in self.gematria if k.isupper()]
		self.lower = [k for k in self.gematria if k.islower()]

		# Mapping for Atbash cipher (reverse the Greek alphabet for uppercase and lowercase separately)
		self.upper_map = {k: self.upper[::-1][i] for i, k in enumerate(self.upper)}
		self.lower_map = {k: self.lower[::-1][i] for i, k in enumerate(self.lower)}
		self.atbash_map = {**self.upper_map, **self.lower_map}

	def normalize_text(self, text):
		"""
		Normalize the text to remove accents and handle Greek characters.
		This converts accented letters to their base (unaccented) form.
		"""
		normalized_text = unicodedata.normalize('NFKD', text)

		# Remove accents by converting the normalized text into its base characters
		return ''.join([c for c in normalized_text if unicodedata.category(c) != 'Mn'])

	def encrypt(self, text: str, case: str = 'upper', rot: int = 0):
		text = self.normalize_text(text)

		# Ensure the text is valid and only contains Greek characters
		if not all(c in self.gematria or c.isspace() for c in text):
			raise ValueError("Text contains non-Greek characters or invalid symbols.")

		# Step 1: Atbash transformation
		atbash_result = [self.atbash_map.get(c, c) for c in text]

		# Step 2: Apply ROT (if any)
		if rot > 0:
			atbash_result = list(self.apply_rot(''.join(atbash_result), rot))

		# Step 3: Case adjustment
		result = ''.join(atbash_result)
		if case == 'upper':
			result = result.upper()
		elif case == 'lower':
			result = result.lower()

		# Gematria calculations
		gem_original = [self.gematria.get(c, 0) for c in text]
		gem_encrypted = [self.gematria.get(c, 0) for c in result]

		# Return both the original and encrypted text, along with gematria values
		return {
			'original': text,
			'encrypted': result,
			'gematria_original': gem_original,
			'gematria_encrypted': gem_encrypted,
			'sum_original': sum(gem_original),
			'sum_encrypted': sum(gem_encrypted),
		}

	def apply_rot(self, text, rot_value):
		if not isinstance(rot_value, int):
			raise ValueError("ROT value must be an integer.")

		# Shift within same case and character type
		def rotate_char(c):
			if c in self.upper:
				index = self.upper.index(c)
				return self.upper[(index + rot_value) % len(self.upper)]
			elif c in self.lower:
				index = self.lower.index(c)
				return self.lower[(index + rot_value) % len(self.lower)]
			return c  # return as-is for spaces or unknowns

		return ''.join(rotate_char(c) for c in text)

	# A rot implication
	def rotate(self, text: str, shift: int, case: str = 'upper'):
		text = self.normalize_text(text)

		if not all(c in self.gematria or c.isspace() for c in text):
			raise ValueError("Text contains non-Greek characters or invalid symbols.")

		rotated = []
		for c in text:
			if c in self.upper:
				index = self.upper.index(c)
				rotated.append(self.upper[(index + shift) % len(self.upper)])
			elif c in self.lower:
				index = self.lower.index(c)
				rotated.append(self.lower[(index + shift) % len(self.lower)])
			else:
				rotated.append(c)

		gem_original = [self.gematria.get(c, 0) for c in text]
		gem_rotated = [self.gematria.get(c, 0) for c in rotated]

		result = ''.join(rotated)
		if case == 'upper':
			result = result.upper()
		elif case == 'lower':
			result = result.lower()

		return {
			'original': text,
			'encrypted': result,
			'gematria_original': gem_original,
			'gematria_encrypted': gem_rotated,
			'sum_original': sum(gem_original),
			'sum_encrypted': sum(gem_rotated),
		}
