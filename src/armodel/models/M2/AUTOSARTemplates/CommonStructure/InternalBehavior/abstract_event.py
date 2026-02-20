"""AbstractEvent AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 541)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 204)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_InternalBehavior.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.InternalBehavior.executable_entity import (
    ExecutableEntity,
)
from abc import ABC, abstractmethod


class AbstractEvent(Identifiable, ABC):
    """AUTOSAR AbstractEvent."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    activation_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize AbstractEvent."""
        super().__init__()
        self.activation_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize AbstractEvent to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractEvent, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize activation_ref
        if self.activation_ref is not None:
            serialized = ARObject._serialize_item(self.activation_ref, "ExecutableEntity")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ACTIVATION-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractEvent":
        """Deserialize XML element to AbstractEvent object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractEvent object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractEvent, cls).deserialize(element)

        # Parse activation_ref
        child = ARObject._find_child_element(element, "ACTIVATION-REF")
        if child is not None:
            activation_ref_value = ARRef.deserialize(child)
            obj.activation_ref = activation_ref_value

        return obj



class AbstractEventBuilder:
    """Builder for AbstractEvent."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: AbstractEvent = AbstractEvent()

    def build(self) -> AbstractEvent:
        """Build and return AbstractEvent object.

        Returns:
            AbstractEvent instance
        """
        # TODO: Add validation
        return self._obj
