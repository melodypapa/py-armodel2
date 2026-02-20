"""ApplicationRecordDataType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 261)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1997)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 34)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_composite_data_type import (
    ApplicationCompositeDataType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject


class ApplicationRecordDataType(ApplicationCompositeDataType):
    """AUTOSAR ApplicationRecordDataType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    elements: list[Any]
    def __init__(self) -> None:
        """Initialize ApplicationRecordDataType."""
        super().__init__()
        self.elements: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize ApplicationRecordDataType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationRecordDataType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize elements (list to container "ELEMENTS")
        if self.elements:
            wrapper = ET.Element("ELEMENTS")
            for item in self.elements:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationRecordDataType":
        """Deserialize XML element to ApplicationRecordDataType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationRecordDataType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationRecordDataType, cls).deserialize(element)

        # Parse elements (list from container "ELEMENTS")
        obj.elements = []
        container = ARObject._find_child_element(element, "ELEMENTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.elements.append(child_value)

        return obj



class ApplicationRecordDataTypeBuilder:
    """Builder for ApplicationRecordDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationRecordDataType = ApplicationRecordDataType()

    def build(self) -> ApplicationRecordDataType:
        """Build and return ApplicationRecordDataType object.

        Returns:
            ApplicationRecordDataType instance
        """
        # TODO: Add validation
        return self._obj
