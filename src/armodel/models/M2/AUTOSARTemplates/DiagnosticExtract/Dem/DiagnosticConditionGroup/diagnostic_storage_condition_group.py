"""DiagnosticStorageConditionGroup AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_DiagnosticExtractTemplate.pdf (page 200)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_DiagnosticExtract_Dem_DiagnosticConditionGroup.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.DiagnosticExtract.Dem.DiagnosticConditionGroup.diagnostic_condition_group import (
    DiagnosticConditionGroup,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef


class DiagnosticStorageConditionGroup(DiagnosticConditionGroup):
    """AUTOSAR DiagnosticStorageConditionGroup."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    storage_refs: list[Any]
    def __init__(self) -> None:
        """Initialize DiagnosticStorageConditionGroup."""
        super().__init__()
        self.storage_refs: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize DiagnosticStorageConditionGroup to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DiagnosticStorageConditionGroup, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize storage_refs (list to container "STORAGE-REFS")
        if self.storage_refs:
            wrapper = ET.Element("STORAGE-REFS")
            for item in self.storage_refs:
                serialized = SerializationHelper.serialize_item(item, "Any")
                if serialized is not None:
                    child_elem = ET.Element("STORAGE-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DiagnosticStorageConditionGroup":
        """Deserialize XML element to DiagnosticStorageConditionGroup object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DiagnosticStorageConditionGroup object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DiagnosticStorageConditionGroup, cls).deserialize(element)

        # Parse storage_refs (list from container "STORAGE-REFS")
        obj.storage_refs = []
        container = SerializationHelper.find_child_element(element, "STORAGE-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.storage_refs.append(child_value)

        return obj



class DiagnosticStorageConditionGroupBuilder:
    """Builder for DiagnosticStorageConditionGroup."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: DiagnosticStorageConditionGroup = DiagnosticStorageConditionGroup()

    def build(self) -> DiagnosticStorageConditionGroup:
        """Build and return DiagnosticStorageConditionGroup object.

        Returns:
            DiagnosticStorageConditionGroup instance
        """
        # TODO: Add validation
        return self._obj
