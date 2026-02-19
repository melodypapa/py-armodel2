"""ExternalTriggeringPoint AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 315)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 584)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_Trigger.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.CommonStructure.TriggerDeclaration.trigger import (
    Trigger,
)


class ExternalTriggeringPoint(ARObject):
    """AUTOSAR ExternalTriggeringPoint."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ident_ref: Optional[ARRef]
    trigger_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize ExternalTriggeringPoint."""
        super().__init__()
        self.ident_ref: Optional[ARRef] = None
        self.trigger_ref: Optional[ARRef] = None
    def serialize(self) -> ET.Element:
        """Serialize ExternalTriggeringPoint to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize ident_ref
        if self.ident_ref is not None:
            serialized = ARObject._serialize_item(self.ident_ref, "ExternalTriggeringPoint")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize trigger_ref
        if self.trigger_ref is not None:
            serialized = ARObject._serialize_item(self.trigger_ref, "Trigger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRIGGER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "ExternalTriggeringPoint":
        """Deserialize XML element to ExternalTriggeringPoint object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ExternalTriggeringPoint object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ident_ref
        child = ARObject._find_child_element(element, "IDENT")
        if child is not None:
            ident_ref_value = ARObject._deserialize_by_tag(child, "ExternalTriggeringPoint")
            obj.ident_ref = ident_ref_value

        # Parse trigger_ref
        child = ARObject._find_child_element(element, "TRIGGER")
        if child is not None:
            trigger_ref_value = ARObject._deserialize_by_tag(child, "Trigger")
            obj.trigger_ref = trigger_ref_value

        return obj



class ExternalTriggeringPointBuilder:
    """Builder for ExternalTriggeringPoint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: ExternalTriggeringPoint = ExternalTriggeringPoint()

    def build(self) -> ExternalTriggeringPoint:
        """Build and return ExternalTriggeringPoint object.

        Returns:
            ExternalTriggeringPoint instance
        """
        # TODO: Add validation
        return self._obj
