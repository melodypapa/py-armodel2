"""RecordValueSpecification AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 328)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 435)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Constants.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Constants.composite_value_specification import (
    CompositeValueSpecification,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class RecordValueSpecification(CompositeValueSpecification):
    """AUTOSAR RecordValueSpecification."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    def __init__(self) -> None:
        """Initialize RecordValueSpecification."""
        super().__init__()

    def serialize(self) -> ET.Element:
        """Serialize RecordValueSpecification to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(RecordValueSpecification, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "RecordValueSpecification":
        """Deserialize XML element to RecordValueSpecification object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized RecordValueSpecification object
        """
        # Delegate to parent class to handle inherited attributes
        return super(RecordValueSpecification, cls).deserialize(element)



class RecordValueSpecificationBuilder:
    """Builder for RecordValueSpecification."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RecordValueSpecification = RecordValueSpecification()

    def build(self) -> RecordValueSpecification:
        """Build and return RecordValueSpecification object.

        Returns:
            RecordValueSpecification instance
        """
        # TODO: Add validation
        return self._obj
