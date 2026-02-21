"""BswEntryRelationship AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 51)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 52)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class BswEntryRelationship(ARObject):
    """AUTOSAR BswEntryRelationship."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_entry: Optional[BswEntryRelationship]
    from_ref: Optional[ARRef]
    to_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize BswEntryRelationship."""
        super().__init__()
        self.bsw_entry: Optional[BswEntryRelationship] = None
        self.from_ref: Optional[ARRef] = None
        self.to_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize BswEntryRelationship to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswEntryRelationship, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_entry
        if self.bsw_entry is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_entry, "BswEntryRelationship")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-ENTRY")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize from_ref
        if self.from_ref is not None:
            serialized = SerializationHelper.serialize_item(self.from_ref, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FROM-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize to_ref
        if self.to_ref is not None:
            serialized = SerializationHelper.serialize_item(self.to_ref, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TO-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswEntryRelationship":
        """Deserialize XML element to BswEntryRelationship object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswEntryRelationship object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswEntryRelationship, cls).deserialize(element)

        # Parse bsw_entry
        child = SerializationHelper.find_child_element(element, "BSW-ENTRY")
        if child is not None:
            bsw_entry_value = SerializationHelper.deserialize_by_tag(child, "BswEntryRelationship")
            obj.bsw_entry = bsw_entry_value

        # Parse from_ref
        child = SerializationHelper.find_child_element(element, "FROM-REF")
        if child is not None:
            from_ref_value = ARRef.deserialize(child)
            obj.from_ref = from_ref_value

        # Parse to_ref
        child = SerializationHelper.find_child_element(element, "TO-REF")
        if child is not None:
            to_ref_value = ARRef.deserialize(child)
            obj.to_ref = to_ref_value

        return obj



class BswEntryRelationshipBuilder:
    """Builder for BswEntryRelationship."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswEntryRelationship = BswEntryRelationship()

    def build(self) -> BswEntryRelationship:
        """Build and return BswEntryRelationship object.

        Returns:
            BswEntryRelationship instance
        """
        # TODO: Add validation
        return self._obj
