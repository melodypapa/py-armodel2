"""CompuScaleRationalFormula AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_contents import (
    CompuScaleContents,
)
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_rational_coeffs import (
    CompuRationalCoeffs,
)


class CompuScaleRationalFormula(CompuScaleContents):
    """AUTOSAR CompuScaleRationalFormula."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("compu_rational_coeffs", None, False, False, CompuRationalCoeffs),  # compuRationalCoeffs
    ]

    def __init__(self) -> None:
        """Initialize CompuScaleRationalFormula."""
        super().__init__()
        self.compu_rational_coeffs: Optional[CompuRationalCoeffs] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert CompuScaleRationalFormula to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuScaleRationalFormula":
        """Create CompuScaleRationalFormula from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            CompuScaleRationalFormula instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to CompuScaleRationalFormula since parent returns ARObject
        return cast("CompuScaleRationalFormula", obj)


class CompuScaleRationalFormulaBuilder:
    """Builder for CompuScaleRationalFormula."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: CompuScaleRationalFormula = CompuScaleRationalFormula()

    def build(self) -> CompuScaleRationalFormula:
        """Build and return CompuScaleRationalFormula object.

        Returns:
            CompuScaleRationalFormula instance
        """
        # TODO: Add validation
        return self._obj
