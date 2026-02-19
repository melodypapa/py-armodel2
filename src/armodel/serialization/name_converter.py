"""Name conversion utility for Python ↔ AUTOSAR XML naming conventions."""


class NameConverter:
    """Convert between Python snake_case and AUTOSAR UPPER-CASE-WITH-HYPHENS naming."""

    @staticmethod
    def to_xml_tag(name: str) -> str:
        """Convert Python attribute or class name to XML tag name.

        Args:
            name: Python attribute name (snake_case) or class name (PascalCase)

        Returns:
            XML tag name (UPPER-CASE-WITH-HYPHENS)

        Examples:
            short_name → SHORT-NAME
            sw_data_def_props → SW-DATA-DEF-PROPS
            ARPackage → ARPACKAGE (AR is exception)
            PackageableElement → PACKAGEABLE-ELEMENT
            SwBaseType → SW-BASE-TYPE
            ImplementationDataType → IMPLEMENTATION-DATA-TYPE
            AUTOSAR → AUTOSAR (all caps stays as one word)
            l1 → L-1 (language-specific element)
            l2 → L-2 (language-specific element)
            l4 → L-4 (language-specific element)
            l5 → L-5 (language-specific element)
            l10 → L-10 (language-specific element)
            timestamp → T (timestamp attribute)
        """
        # Special case for timestamp attribute
        if name == 'timestamp':
            return "T"

        # Handle language-specific elements (l1, l2, l3, l4, l5, l10)
        if name in ['l1', 'l2', 'l3', 'l4', 'l5']:
            return f"L-{name[1]}"
        if name == 'l10':
            return "L-10"

        # Handle snake_case attributes (existing logic)
        if '_' in name:
            # Remove private prefix
            if name.startswith('_'):
                name = name[1:]
            # Convert to uppercase and replace underscores with hyphens
            return name.upper().replace('_', '-')

        # Handle PascalCase class names
        # If all uppercase, return as-is (e.g., AUTOSAR)
        if name.isupper():
            return name

        # Split camelCase into words
        words = []
        current_word = ""

        for i, char in enumerate(name):
            if char.isupper():
                if current_word:
                    words.append(current_word)
                current_word = char
            else:
                current_word += char

        if current_word:
            words.append(current_word)

        # Handle AR prefix exception
        # If first word is "A" and second is "R", combine them
        if len(words) >= 2 and words[0] == "A" and words[1] == "R":
            # Combine A and R into AR
            words[0] = "AR"
            words.pop(1)
        elif len(words) >= 2 and words[0] == "AR" and words[1][0].isupper():
            # AR is already combined, keep it separate
            pass

        # Join with hyphens and convert to uppercase
        return '-'.join(words).upper()

    @staticmethod
    def to_python_name(tag: str) -> str:
        """Convert XML tag name to Python attribute name.

        Args:
            tag: XML tag name (UPPER-CASE-WITH-HYPHENS)

        Returns:
            Python attribute name (snake_case)

        Examples:
            SHORT-NAME → short_name
            SW-DATA-DEF-PROPS → sw_data_def_props
            L-1 → l1 (language-specific element)
            L-2 → l2 (language-specific element)
            L-4 → l4 (language-specific element)
            L-5 → l5 (language-specific element)
            L-10 → l10 (language-specific element)
            T → timestamp (timestamp attribute)
        """
        # Special case for timestamp attribute
        if tag == 'T':
            return "timestamp"

        # Handle language-specific elements (L-1, L-2, L-3, L-4, L-5, L-10)
        if tag in ['L-1', 'L-2', 'L-3', 'L-4', 'L-5']:
            return f"l{tag[2]}"
        if tag == 'L-10':
            return "l10"

        return tag.lower().replace('-', '_')

    @staticmethod
    def to_singular(tag: str) -> str:
        """Convert plural XML tag to singular form.

        Args:
            tag: Plural XML tag name (UPPER-CASE-WITH-HYPHENS)

        Returns:
            Singular XML tag name

        Examples:
            AR-PACKAGES → AR-PACKAGE
            ELEMENTS → ELEMENT
            PACKAGES → PACKAGE
        """
        # Simple plural rules for AUTOSAR
        if tag.endswith('S'):
            # Remove trailing 'S' for simple plurals
            return tag[:-1]
        return tag

    @staticmethod
    def tag_to_class_name(tag: str) -> str:
        """Convert XML tag name to Python class name.

        Args:
            tag: XML tag name (UPPER-CASE-WITH-HYPHENS)

        Returns:
            Python class name (PascalCase)

        Examples:
            SW-BASE-TYPE → SwBaseType
            IMPLEMENTATION-DATA-TYPE → ImplementationDataType
            AR-PACKAGE → ARPackage
            AUTOSAR → AUTOSAR
            SHORT-NAME → ShortName
        """
        # Split by hyphen
        words = tag.split('-')

        # Handle all-caps single words (e.g., CATEGORY → Category)
        if len(words) == 1 and words[0].isupper():
            # Keep known acronyms as-is
            if words[0] in ['AUTOSAR', 'AR', 'AUTOSAR']:
                return words[0]
            # Convert normal words to PascalCase
            return words[0].capitalize()

        # Handle AR prefix exception - keep AR as uppercase
        if words[0] == 'AR':
            # Keep AR as uppercase
            pass

        # Capitalize each word and join
        class_name = ''.join(word.capitalize() for word in words)

        # Fix AR prefix - ensure it's uppercase
        if class_name.startswith('Ar'):
            class_name = 'AR' + class_name[2:]

        return class_name