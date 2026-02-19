"""CompuRationalCoeffs AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 389)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.MSR.AsamHdo.ComputationMethod.compu_nominator_denominator import (
    CompuNominatorDenominator,
)


class CompuRationalCoeffs(ARObject):
    """AUTOSAR CompuRationalCoeffs."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    compu_denominator: Optional[CompuNominatorDenominator]
    compu: Optional[CompuNominatorDenominator]
    def __init__(self) -> None:
        """Initialize CompuRationalCoeffs."""
        super().__init__()
        self.compu_denominator: Optional[CompuNominatorDenominator] = None
        self.compu: Optional[CompuNominatorDenominator] = None
    def serialize(self) -> ET.Element:
        """Serialize CompuRationalCoeffs to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize compu_denominator
        if self.compu_denominator is not None:
            serialized = ARObject._serialize_item(self.compu_denominator, "CompuNominatorDenominator")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPU-DENOMINATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize compu
        if self.compu is not None:
            serialized = ARObject._serialize_item(self.compu, "CompuNominatorDenominator")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPU")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuRationalCoeffs":
        """Deserialize XML element to CompuRationalCoeffs object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuRationalCoeffs object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse compu_denominator
        child = ARObject._find_child_element(element, "COMPU-DENOMINATOR")
        if child is not None:
            compu_denominator_value = ARObject._deserialize_by_tag(child, "CompuNominatorDenominator")
            obj.compu_denominator = compu_denominator_value

        # Parse compu
        child = ARObject._find_child_element(element, "COMPU")
        if child is not None:
            compu_value = ARObject._deserialize_by_tag(child, "CompuNominatorDenominator")
            obj.compu = compu_value

        return obj



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
