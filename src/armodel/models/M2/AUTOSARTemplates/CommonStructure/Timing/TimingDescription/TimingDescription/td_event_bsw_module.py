"""TDEventBswModule AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 75)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_Timing_TimingDescription_TimingDescription.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.CommonStructure.Timing.TimingDescription.TimingDescription.td_event_bsw import (
    TDEventBsw,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswInterfaces.bsw_module_entry import (
    BswModuleEntry,
)


class TDEventBswModule(TDEventBsw):
    """AUTOSAR TDEventBswModule."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_module_entry_entry_ref: Optional[ARRef]
    td_event_bsw: Optional[TDEventBswModule]
    def __init__(self) -> None:
        """Initialize TDEventBswModule."""
        super().__init__()
        self.bsw_module_entry_entry_ref: Optional[ARRef] = None
        self.td_event_bsw: Optional[TDEventBswModule] = None

    def serialize(self) -> ET.Element:
        """Serialize TDEventBswModule to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(TDEventBswModule, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_module_entry_entry_ref
        if self.bsw_module_entry_entry_ref is not None:
            serialized = ARObject._serialize_item(self.bsw_module_entry_entry_ref, "BswModuleEntry")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-MODULE-ENTRY-ENTRY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize td_event_bsw
        if self.td_event_bsw is not None:
            serialized = ARObject._serialize_item(self.td_event_bsw, "TDEventBswModule")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TD-EVENT-BSW")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "TDEventBswModule":
        """Deserialize XML element to TDEventBswModule object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized TDEventBswModule object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(TDEventBswModule, cls).deserialize(element)

        # Parse bsw_module_entry_entry_ref
        child = ARObject._find_child_element(element, "BSW-MODULE-ENTRY-ENTRY-REF")
        if child is not None:
            bsw_module_entry_entry_ref_value = ARRef.deserialize(child)
            obj.bsw_module_entry_entry_ref = bsw_module_entry_entry_ref_value

        # Parse td_event_bsw
        child = ARObject._find_child_element(element, "TD-EVENT-BSW")
        if child is not None:
            td_event_bsw_value = ARObject._deserialize_by_tag(child, "TDEventBswModule")
            obj.td_event_bsw = td_event_bsw_value

        return obj



class TDEventBswModuleBuilder:
    """Builder for TDEventBswModule."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: TDEventBswModule = TDEventBswModule()

    def build(self) -> TDEventBswModule:
        """Build and return TDEventBswModule object.

        Returns:
            TDEventBswModule instance
        """
        # TODO: Add validation
        return self._obj
