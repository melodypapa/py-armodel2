"""CompuRationalCoeffs AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 389)

JSON Source: docs/json/packages/M2_MSR_AsamHdo_ComputationMethod.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
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

    compu_numerator: Optional[CompuNominatorDenominator]
    compu_denominator: Optional[CompuNominatorDenominator]
    def __init__(self) -> None:
        """Initialize CompuRationalCoeffs."""
        super().__init__()
        self.compu_numerator: Optional[CompuNominatorDenominator] = None
        self.compu_denominator: Optional[CompuNominatorDenominator] = None

    def serialize(self) -> ET.Element:
        """Serialize CompuRationalCoeffs to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(CompuRationalCoeffs, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize compu_numerator
        if self.compu_numerator is not None:
            serialized = SerializationHelper.serialize_item(self.compu_numerator, "CompuNominatorDenominator")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COMPU-NUMERATOR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize compu_denominator
        if self.compu_denominator is not None:
            serialized = SerializationHelper.serialize_item(self.compu_denominator, "CompuNominatorDenominator")
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

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "CompuRationalCoeffs":
        """Deserialize XML element to CompuRationalCoeffs object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized CompuRationalCoeffs object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(CompuRationalCoeffs, cls).deserialize(element)

        # Parse compu_numerator
        child = SerializationHelper.find_child_element(element, "COMPU-NUMERATOR")
        if child is not None:
            compu_numerator_value = SerializationHelper.deserialize_by_tag(child, "CompuNominatorDenominator")
            obj.compu_numerator = compu_numerator_value

        # Parse compu_denominator
        child = SerializationHelper.find_child_element(element, "COMPU-DENOMINATOR")
        if child is not None:
            compu_denominator_value = SerializationHelper.deserialize_by_tag(child, "CompuNominatorDenominator")
            obj.compu_denominator = compu_denominator_value

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
