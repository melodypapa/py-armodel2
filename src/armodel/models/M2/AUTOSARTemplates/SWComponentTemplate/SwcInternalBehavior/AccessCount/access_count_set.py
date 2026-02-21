"""AccessCountSet AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_AccessCount.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    NameToken,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.AccessCount.access_count import (
    AccessCount,
)


class AccessCountSet(ARObject):
    """AUTOSAR AccessCountSet."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    access_counts: list[AccessCount]
    count_profile: Optional[NameToken]
    def __init__(self) -> None:
        """Initialize AccessCountSet."""
        super().__init__()
        self.access_counts: list[AccessCount] = []
        self.count_profile: Optional[NameToken] = None

    def serialize(self) -> ET.Element:
        """Serialize AccessCountSet to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AccessCountSet, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize access_counts (list to container "ACCESS-COUNTS")
        if self.access_counts:
            wrapper = ET.Element("ACCESS-COUNTS")
            for item in self.access_counts:
                serialized = SerializationHelper.serialize_item(item, "AccessCount")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize count_profile
        if self.count_profile is not None:
            serialized = SerializationHelper.serialize_item(self.count_profile, "NameToken")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("COUNT-PROFILE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AccessCountSet":
        """Deserialize XML element to AccessCountSet object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AccessCountSet object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AccessCountSet, cls).deserialize(element)

        # Parse access_counts (list from container "ACCESS-COUNTS")
        obj.access_counts = []
        container = SerializationHelper.find_child_element(element, "ACCESS-COUNTS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.access_counts.append(child_value)

        # Parse count_profile
        child = SerializationHelper.find_child_element(element, "COUNT-PROFILE")
        if child is not None:
            count_profile_value = child.text
            obj.count_profile = count_profile_value

        return obj



class AccessCountSetBuilder:
    """Builder for AccessCountSet."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AccessCountSet = AccessCountSet()

    def build(self) -> AccessCountSet:
        """Build and return AccessCountSet object.

        Returns:
            AccessCountSet instance
        """
        # TODO: Add validation
        return self._obj
