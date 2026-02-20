"""ApplicationArrayDataType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 252)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 1995)
  - AUTOSAR_FO_TPS_AbstractPlatformSpecification.pdf (page 35)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Datatype_Datatypes.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.Datatypes.application_composite_data_type import (
    ApplicationCompositeDataType,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    String,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.application_array_element import (
    ApplicationArrayElement,
)


class ApplicationArrayDataType(ApplicationCompositeDataType):
    """AUTOSAR ApplicationArrayDataType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    dynamic_array_size_profile: Optional[String]
    element: Optional[ApplicationArrayElement]
    def __init__(self) -> None:
        """Initialize ApplicationArrayDataType."""
        super().__init__()
        self.dynamic_array_size_profile: Optional[String] = None
        self.element: Optional[ApplicationArrayElement] = None

    def serialize(self) -> ET.Element:
        """Serialize ApplicationArrayDataType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ApplicationArrayDataType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize dynamic_array_size_profile
        if self.dynamic_array_size_profile is not None:
            serialized = ARObject._serialize_item(self.dynamic_array_size_profile, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DYNAMIC-ARRAY-SIZE-PROFILE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize element
        if self.element is not None:
            serialized = ARObject._serialize_item(self.element, "ApplicationArrayElement")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ELEMENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ApplicationArrayDataType":
        """Deserialize XML element to ApplicationArrayDataType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ApplicationArrayDataType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ApplicationArrayDataType, cls).deserialize(element)

        # Parse dynamic_array_size_profile
        child = ARObject._find_child_element(element, "DYNAMIC-ARRAY-SIZE-PROFILE")
        if child is not None:
            dynamic_array_size_profile_value = child.text
            obj.dynamic_array_size_profile = dynamic_array_size_profile_value

        # Parse element
        child = ARObject._find_child_element(element, "ELEMENT")
        if child is not None:
            element_value = ARObject._deserialize_by_tag(child, "ApplicationArrayElement")
            obj.element = element_value

        return obj



class ApplicationArrayDataTypeBuilder:
    """Builder for ApplicationArrayDataType."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ApplicationArrayDataType = ApplicationArrayDataType()

    def build(self) -> ApplicationArrayDataType:
        """Build and return ApplicationArrayDataType object.

        Returns:
            ApplicationArrayDataType instance
        """
        # TODO: Add validation
        return self._obj
