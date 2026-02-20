"""BswEntryRelationship AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 51)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 52)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswInterfaces.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
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
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize bsw_entry
        if self.bsw_entry is not None:
            serialized = ARObject._serialize_item(self.bsw_entry, "BswEntryRelationship")
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
            serialized = ARObject._serialize_item(self.from_ref, "BswModuleEntry")
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
            serialized = ARObject._serialize_item(self.to_ref, "BswModuleEntry")
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
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse bsw_entry
        child = ARObject._find_child_element(element, "BSW-ENTRY")
        if child is not None:
            bsw_entry_value = ARObject._deserialize_by_tag(child, "BswEntryRelationship")
            obj.bsw_entry = bsw_entry_value

        # Parse from_ref
        child = ARObject._find_child_element(element, "FROM-REF")
        if child is not None:
            from_ref_value = ARRef.deserialize(child)
            obj.from_ref = from_ref_value

        # Parse to_ref
        child = ARObject._find_child_element(element, "TO-REF")
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
