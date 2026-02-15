"""ARPackage AUTOSAR element."""

from typing import Any

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import (
    ARObject,
)
import xml.etree.ElementTree as ET


class ARPackage(ARObject):
    """AUTOSAR ARPackage."""

    def __init__(self) -> None:
        """Initialize ARPackage."""
        super().__init__()
        self.short_name: str = ""
        self.long_name: str = ""
        self.category: str = ""
        self.reference_bases: list[Any] = []
        self.elements: list[Any] = []
        self.ar_packages: list[Any] = []

    def serialize(self, namespace: str = "http://autosar.org/schema/r4.0") -> ET.Element:
        """Convert ARPackage to XML element with proper namespace handling.

        Args:
            namespace: XML namespace URI to use for elements

        Returns:
            XML element representing this object
        """
        element = ET.Element(f"{{{namespace}}}AR-PACKAGE")

        # SHORT-NAME
        if self.short_name:
            short_name_elem = ET.SubElement(element, f"{{{namespace}}}SHORT-NAME")
            short_name_elem.text = self.short_name

        # LONG-NAME
        if self.long_name:
            long_name_elem = ET.SubElement(element, f"{{{namespace}}}LONG-NAME")
            l4_elem = ET.SubElement(long_name_elem, f"{{{namespace}}}L-4")
            l4_elem.set("L", "EN")
            l4_elem.text = self.long_name

        # CATEGORY
        if self.category:
            category_elem = ET.SubElement(element, f"{{{namespace}}}CATEGORY")
            category_elem.text = self.category

        # REFERENCE-BASES
        if self.reference_bases:
            ref_bases_elem = ET.SubElement(element, f"{{{namespace}}}REFERENCE-BASES")
            for ref_base in self.reference_bases:
                if hasattr(ref_base, "serialize"):
                    ref_bases_elem.append(ref_base.serialize(namespace))

        # ELEMENTS
        if self.elements:
            elements_elem = ET.SubElement(element, f"{{{namespace}}}ELEMENTS")
            for elem in self.elements:
                if hasattr(elem, "serialize"):
                    elements_elem.append(elem.serialize(namespace))

        # AR-PACKAGES (nested packages)
        if self.ar_packages:
            packages_elem = ET.SubElement(element, f"{{{namespace}}}AR-PACKAGES")
            for pkg in self.ar_packages:
                if hasattr(pkg, "serialize"):
                    packages_elem.append(pkg.serialize(namespace))

        return element

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ARPackage":
        """Create ARPackage from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            ARPackage instance
        """
        obj: ARPackage = cls()

        for child in element:
            tag_name = child.tag.split("}")[-1] if "}" in child.tag else child.tag

            if tag_name == "SHORT-NAME":
                obj.short_name = child.text or ""
            elif tag_name == "LONG-NAME":
                # Handle L-4 elements with language
                l_elem = child.find(".//{*}L-4")
                if l_elem is not None and l_elem.text:
                    obj.long_name = l_elem.text
                elif child.text:
                    obj.long_name = child.text
            elif tag_name == "CATEGORY":
                obj.category = child.text or ""
            elif tag_name == "REFERENCE-BASES":
                # TODO: Parse reference bases
                pass
            elif tag_name == "ELEMENTS":
                # TODO: Parse elements (Application Data Types, etc.)
                pass
            elif tag_name == "AR-PACKAGES":
                # Recursively deserialize nested packages
                for pkg_elem in child:
                    if pkg_elem.tag.endswith("AR-PACKAGE"):
                        pkg = cls.deserialize(pkg_elem)
                        obj.ar_packages.append(pkg)

        return obj


class ARPackageBuilder:
    """Builder for ARPackage."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ARPackage = ARPackage()

    def build(self) -> ARPackage:
        """Build and return ARPackage object.

        Returns:
            ARPackage instance
        """
        # TODO: Add validation
        return self._obj
