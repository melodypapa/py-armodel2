"""TDEventModeDeclaration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 57)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_vfb_port import (
    TDEventVfbPort,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class TDEventModeDeclaration(TDEventVfbPort):
    """AUTOSAR TDEventModeDeclaration."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    entry_mode_ref: Optional[ARRef]
    exit_mode_ref: Optional[ARRef]
    mode_ref: Optional[ARRef]
    td_event_mode: Optional[Any]
    def __init__(self) -> None:
        """Initialize TDEventModeDeclaration."""
        super().__init__()
        self.entry_mode_ref: Optional[ARRef] = None
        self.exit_mode_ref: Optional[ARRef] = None
        self.mode_ref: Optional[ARRef] = None
        self.td_event_mode: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventModeDeclaration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventModeDeclaration, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize entry_mode_ref
        if self.entry_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.entry_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENTRY-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize exit_mode_ref
        if self.exit_mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.exit_mode_ref, "ModeDeclaration")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("EXIT-MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mode_ref
        if self.mode_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mode_ref, "ModeDeclarationGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MODE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_event_mode
        if self.td_event_mode is not None:
            serialized = SerializationHelper.serialize_item(self.td_event_mode, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-MODE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventModeDeclaration":
        """Deserialize XML element to TDEventModeDeclaration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventModeDeclaration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventModeDeclaration, cls).deserialize(element)

        # Parse entry_mode_ref
        child = SerializationHelper.find_child_element(element, "ENTRY-MODE-REF")
        if child is not None:
            entry_mode_ref_value = ARRef.deserialize(child)
            obj.entry_mode_ref = entry_mode_ref_value

        # Parse exit_mode_ref
        child = SerializationHelper.find_child_element(element, "EXIT-MODE-REF")
        if child is not None:
            exit_mode_ref_value = ARRef.deserialize(child)
            obj.exit_mode_ref = exit_mode_ref_value

        # Parse mode_ref
        child = SerializationHelper.find_child_element(element, "MODE-REF")
        if child is not None:
            mode_ref_value = ARRef.deserialize(child)
            obj.mode_ref = mode_ref_value

        # Parse td_event_mode
        child = SerializationHelper.find_child_element(element, "TD-EVENT-MODE")
        if child is not None:
            td_event_mode_value = child.text
            obj.td_event_mode = td_event_mode_value

        return obj



class TDEventModeDeclarationBuilder:
    """Builder for TDEventModeDeclaration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventModeDeclaration = TDEventModeDeclaration()

    def build(self) -> TDEventModeDeclaration:
        """Build and return TDEventModeDeclaration object.

        Returns:
            TDEventModeDeclaration instance
        """
        # TODO: Add validation
        return self._obj
