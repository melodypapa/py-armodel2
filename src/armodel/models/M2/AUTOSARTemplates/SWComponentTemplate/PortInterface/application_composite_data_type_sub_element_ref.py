"""ApplicationCompositeDataTypeSubElementRef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 138)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.sub_element_ref import (
    SubElementRef,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper


class ApplicationCompositeDataTypeSubElementRef(SubElementRef):
    """AUTOSAR ApplicationCompositeDataTypeSubElementRef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    application: Optional[Any]
    def __init__(self) -> None:
        """Initialize ApplicationCompositeDataTypeSubElementRef."""
        super().__init__()
        self.application: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize ApplicationCompositeDataTypeSubElementRef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationCompositeDataTypeSubElementRef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize application
        if self.application is not None:
            serialized = SerializationHelper.serialize_item(self.application, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("APPLICATION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationCompositeDataTypeSubElementRef":
        """Deserialize XML element to ApplicationCompositeDataTypeSubElementRef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationCompositeDataTypeSubElementRef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationCompositeDataTypeSubElementRef, cls).deserialize(element)

        # Parse application
        child = SerializationHelper.find_child_element(element, "APPLICATION")
        if child is not None:
            application_value = child.text
            obj.application = application_value

        return obj



class ApplicationCompositeDataTypeSubElementRefBuilder:
    """Builder for ApplicationCompositeDataTypeSubElementRef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationCompositeDataTypeSubElementRef = ApplicationCompositeDataTypeSubElementRef()

    def build(self) -> ApplicationCompositeDataTypeSubElementRef:
        """Build and return ApplicationCompositeDataTypeSubElementRef object.

        Returns:
            ApplicationCompositeDataTypeSubElementRef instance
        """
        # TODO: Add validation
        return self._obj
