"""SignalServiceTranslationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 336)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1005)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 730)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_CommonStructure_SignalServiceTranslation.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional, Any
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.consumed_event_group import (
    ConsumedEventGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.event_handler import (
    EventHandler,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.PncMapping.pnc_mapping_ident import (
    PncMappingIdent,
)


class SignalServiceTranslationProps(Identifiable):
    """AUTOSAR SignalServiceTranslationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    control_refs: list[ARRef]
    control_pnc_refs: list[ARRef]
    control_provideds: list[EventHandler]
    service_control: Optional[Any]
    signal_service_event_propses: list[Any]
    def __init__(self) -> None:
        """Initialize SignalServiceTranslationProps."""
        super().__init__()
        self.control_refs: list[ARRef] = []
        self.control_pnc_refs: list[ARRef] = []
        self.control_provideds: list[EventHandler] = []
        self.service_control: Optional[Any] = None
        self.signal_service_event_propses: list[Any] = []
    def serialize(self) -> ET.Element:
        """Serialize SignalServiceTranslationProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SignalServiceTranslationProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize control_refs (list to container "CONTROLS")
        if self.control_refs:
            wrapper = ET.Element("CONTROLS")
            for item in self.control_refs:
                serialized = ARObject._serialize_item(item, "ConsumedEventGroup")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize control_pnc_refs (list to container "CONTROL-PNCS")
        if self.control_pnc_refs:
            wrapper = ET.Element("CONTROL-PNCS")
            for item in self.control_pnc_refs:
                serialized = ARObject._serialize_item(item, "PncMappingIdent")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize control_provideds (list to container "CONTROL-PROVIDEDS")
        if self.control_provideds:
            wrapper = ET.Element("CONTROL-PROVIDEDS")
            for item in self.control_provideds:
                serialized = ARObject._serialize_item(item, "EventHandler")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize service_control
        if self.service_control is not None:
            serialized = ARObject._serialize_item(self.service_control, "Any")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SERVICE-CONTROL")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize signal_service_event_propses (list to container "SIGNAL-SERVICE-EVENT-PROPSES")
        if self.signal_service_event_propses:
            wrapper = ET.Element("SIGNAL-SERVICE-EVENT-PROPSES")
            for item in self.signal_service_event_propses:
                serialized = ARObject._serialize_item(item, "Any")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SignalServiceTranslationProps":
        """Deserialize XML element to SignalServiceTranslationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SignalServiceTranslationProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SignalServiceTranslationProps, cls).deserialize(element)

        # Parse control_refs (list from container "CONTROLS")
        obj.control_refs = []
        container = ARObject._find_child_element(element, "CONTROLS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.control_refs.append(child_value)

        # Parse control_pnc_refs (list from container "CONTROL-PNCS")
        obj.control_pnc_refs = []
        container = ARObject._find_child_element(element, "CONTROL-PNCS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.control_pnc_refs.append(child_value)

        # Parse control_provideds (list from container "CONTROL-PROVIDEDS")
        obj.control_provideds = []
        container = ARObject._find_child_element(element, "CONTROL-PROVIDEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.control_provideds.append(child_value)

        # Parse service_control
        child = ARObject._find_child_element(element, "SERVICE-CONTROL")
        if child is not None:
            service_control_value = child.text
            obj.service_control = service_control_value

        # Parse signal_service_event_propses (list from container "SIGNAL-SERVICE-EVENT-PROPSES")
        obj.signal_service_event_propses = []
        container = ARObject._find_child_element(element, "SIGNAL-SERVICE-EVENT-PROPSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.signal_service_event_propses.append(child_value)

        return obj



class SignalServiceTranslationPropsBuilder:
    """Builder for SignalServiceTranslationProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SignalServiceTranslationProps = SignalServiceTranslationProps()

    def build(self) -> SignalServiceTranslationProps:
        """Build and return SignalServiceTranslationProps object.

        Returns:
            SignalServiceTranslationProps instance
        """
        # TODO: Add validation
        return self._obj
