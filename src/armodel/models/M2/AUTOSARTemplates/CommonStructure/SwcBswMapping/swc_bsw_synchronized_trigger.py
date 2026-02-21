"""SwcBswSynchronizedTrigger AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 111)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SwcBswMapping.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class SwcBswSynchronizedTrigger(ARObject):
    """AUTOSAR SwcBswSynchronizedTrigger."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    bsw_trigger_ref: Optional[ARRef]
    swc_trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwcBswSynchronizedTrigger."""
        super().__init__()
        self.bsw_trigger_ref: Optional[ARRef] = None
        self.swc_trigger_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwcBswSynchronizedTrigger to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwcBswSynchronizedTrigger, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize bsw_trigger_ref
        if self.bsw_trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.bsw_trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("BSW-TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize swc_trigger_ref
        if self.swc_trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.swc_trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SWC-TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwcBswSynchronizedTrigger":
        """Deserialize XML element to SwcBswSynchronizedTrigger object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwcBswSynchronizedTrigger object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwcBswSynchronizedTrigger, cls).deserialize(element)

        # Parse bsw_trigger_ref
        child = SerializationHelper.find_child_element(element, "BSW-TRIGGER-REF")
        if child is not None:
            bsw_trigger_ref_value = ARRef.deserialize(child)
            obj.bsw_trigger_ref = bsw_trigger_ref_value

        # Parse swc_trigger_ref
        child = SerializationHelper.find_child_element(element, "SWC-TRIGGER-REF")
        if child is not None:
            swc_trigger_ref_value = ARRef.deserialize(child)
            obj.swc_trigger_ref = swc_trigger_ref_value

        return obj



class SwcBswSynchronizedTriggerBuilder:
    """Builder for SwcBswSynchronizedTrigger."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwcBswSynchronizedTrigger = SwcBswSynchronizedTrigger()

    def build(self) -> SwcBswSynchronizedTrigger:
        """Build and return SwcBswSynchronizedTrigger object.

        Returns:
            SwcBswSynchronizedTrigger instance
        """
        # TODO: Add validation
        return self._obj
