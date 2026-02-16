"""CompuRationalCoeffs AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_nominator_denominator import (
    CompuNominatorDenominator,
)


class CompuRationalCoeffs(ARObject):
    """AUTOSAR CompuRationalCoeffs."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("compu_denominator", None, False, False, CompuNominatorDenominator),  # compuDenominator
        ("compu", None, False, False, CompuNominatorDenominator),  # compu
    ]

    def __init__(self) -> None:
        """Initialize CompuRationalCoeffs."""
        super().__init__()
        self.compu_denominator: Optional[CompuNominatorDenominator] = None
        self.compu: Optional[CompuNominatorDenominator] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CompuRationalCoeffs to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuRationalCoeffs":
        """Create CompuRationalCoeffs from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CompuRationalCoeffs instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CompuRationalCoeffs since parent returns ARObject
        return cast("CompuRationalCoeffs", obj)


class CompuRationalCoeffsBuilder:
    """Builder for CompuRationalCoeffs."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuRationalCoeffs = CompuRationalCoeffs()

    def build(self) -> CompuRationalCoeffs:
        """Build and return CompuRationalCoeffs object.

        Returns:
            CompuRationalCoeffs instance
        """
        # TODO: Add validation
        return self._obj
