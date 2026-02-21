"""TDEventBswModeDeclaration AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 76)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw import (
    TDEventBsw,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration import (
    ModeDeclaration,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.ModeDeclaration.mode_declaration_group import (
    ModeDeclarationGroup,
)


class TDEventBswModeDeclaration(TDEventBsw):
    """AUTOSAR TDEventBswModeDeclaration."""

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
    td_event_bsw_declaration_type: Optional[Any]
    def __init__(self) -> None:
        """Initialize TDEventBswModeDeclaration."""
        super().__init__()
        self.entry_mode_ref: Optional[ARRef] = None
        self.exit_mode_ref: Optional[ARRef] = None
        self.mode_ref: Optional[ARRef] = None
        self.td_event_bsw_declaration_type: Optional[Any] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventBswModeDeclaration to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventBswModeDeclaration, self).serialize()

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
            serialized = ARObject._serialize_item(self.entry_mode_ref, "ModeDeclaration")
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
            serialized = ARObject._serialize_item(self.exit_mode_ref, "ModeDeclaration")
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
            serialized = ARObject._serialize_item(self.mode_ref, "ModeDeclarationGroup")
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

        # Serialize td_event_bsw_declaration_type
        if self.td_event_bsw_declaration_type is not None:
            serialized = ARObject._serialize_item(self.td_event_bsw_declaration_type, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-BSW-DECLARATION-TYPE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventBswModeDeclaration":
        """Deserialize XML element to TDEventBswModeDeclaration object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventBswModeDeclaration object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventBswModeDeclaration, cls).deserialize(element)

        # Parse entry_mode_ref
        child = ARObject._find_child_element(element, "ENTRY-MODE-REF")
        if child is not None:
            entry_mode_ref_value = ARRef.deserialize(child)
            obj.entry_mode_ref = entry_mode_ref_value

        # Parse exit_mode_ref
        child = ARObject._find_child_element(element, "EXIT-MODE-REF")
        if child is not None:
            exit_mode_ref_value = ARRef.deserialize(child)
            obj.exit_mode_ref = exit_mode_ref_value

        # Parse mode_ref
        child = ARObject._find_child_element(element, "MODE-REF")
        if child is not None:
            mode_ref_value = ARRef.deserialize(child)
            obj.mode_ref = mode_ref_value

        # Parse td_event_bsw_declaration_type
        child = ARObject._find_child_element(element, "TD-EVENT-BSW-DECLARATION-TYPE")
        if child is not None:
            td_event_bsw_declaration_type_value = child.text
            obj.td_event_bsw_declaration_type = td_event_bsw_declaration_type_value

        return obj



class TDEventBswModeDeclarationBuilder:
    """Builder for TDEventBswModeDeclaration."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventBswModeDeclaration = TDEventBswModeDeclaration()

    def build(self) -> TDEventBswModeDeclaration:
        """Build and return TDEventBswModeDeclaration object.

        Returns:
            TDEventBswModeDeclaration instance
        """
        # TODO: Add validation
        return self._obj
