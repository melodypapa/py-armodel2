"""CompuScaleRationalFormula AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 390)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_scale_contents import (
    CompuScaleContents,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_rational_coeffs import (
    CompuRationalCoeffs,
)


class CompuScaleRationalFormula(CompuScaleContents):
    """AUTOSAR CompuScaleRationalFormula."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compu_rational_coeffs: Optional[CompuRationalCoeffs]
    def __init__(self) -> None:
        """Initialize CompuScaleRationalFormula."""
        super().__init__()
        self.compu_rational_coeffs: Optional[CompuRationalCoeffs] = None
    def serialize(self) -> ET.Element:
        """Serialize CompuScaleRationalFormula to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CompuScaleRationalFormula, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize compu_rational_coeffs
        if self.compu_rational_coeffs is not None:
            serialized = ARObject._serialize_item(self.compu_rational_coeffs, "CompuRationalCoeffs")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPU-RATIONAL-COEFFS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuScaleRationalFormula":
        """Deserialize XML element to CompuScaleRationalFormula object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuScaleRationalFormula object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CompuScaleRationalFormula, cls).deserialize(element)

        # Parse compu_rational_coeffs
        child = ARObject._find_child_element(element, "COMPU-RATIONAL-COEFFS")
        if child is not None:
            compu_rational_coeffs_value = ARObject._deserialize_by_tag(child, "CompuRationalCoeffs")
            obj.compu_rational_coeffs = compu_rational_coeffs_value

        return obj



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
