"""BswTriggerDirectImplementation AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 102)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_BswModuleTemplate_BswBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class BswTriggerDirectImplementation(ARObject):
    """AUTOSAR BswTriggerDirectImplementation."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    cat2_isr: Optional[Identifier]
    mastered_trigger_ref: Optional[ARRef]
    task: Optional[Identifier]
    def __init__(self) -> None:
        """Initialize BswTriggerDirectImplementation."""
        super().__init__()
        self.cat2_isr: Optional[Identifier] = None
        self.mastered_trigger_ref: Optional[ARRef] = None
        self.task: Optional[Identifier] = None

    def serialize(self) -> ET.Element:
        """Serialize BswTriggerDirectImplementation to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(BswTriggerDirectImplementation, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize cat2_isr
        if self.cat2_isr is not None:
            serialized = SerializationHelper.serialize_item(self.cat2_isr, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CAT2-ISR")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mastered_trigger_ref
        if self.mastered_trigger_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mastered_trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MASTERED-TRIGGER-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize task
        if self.task is not None:
            serialized = SerializationHelper.serialize_item(self.task, "Identifier")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TASK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswTriggerDirectImplementation":
        """Deserialize XML element to BswTriggerDirectImplementation object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized BswTriggerDirectImplementation object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(BswTriggerDirectImplementation, cls).deserialize(element)

        # Parse cat2_isr
        child = SerializationHelper.find_child_element(element, "CAT2-ISR")
        if child is not None:
            cat2_isr_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.cat2_isr = cat2_isr_value

        # Parse mastered_trigger_ref
        child = SerializationHelper.find_child_element(element, "MASTERED-TRIGGER-REF")
        if child is not None:
            mastered_trigger_ref_value = ARRef.deserialize(child)
            obj.mastered_trigger_ref = mastered_trigger_ref_value

        # Parse task
        child = SerializationHelper.find_child_element(element, "TASK")
        if child is not None:
            task_value = SerializationHelper.deserialize_by_tag(child, "Identifier")
            obj.task = task_value

        return obj



class BswTriggerDirectImplementationBuilder:
    """Builder for BswTriggerDirectImplementation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswTriggerDirectImplementation = BswTriggerDirectImplementation()

    def build(self) -> BswTriggerDirectImplementation:
        """Build and return BswTriggerDirectImplementation object.

        Returns:
            BswTriggerDirectImplementation instance
        """
        # TODO: Add validation
        return self._obj
