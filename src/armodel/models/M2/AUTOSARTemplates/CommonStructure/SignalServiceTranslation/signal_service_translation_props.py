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
from armodel.serialization import SerializationHelper
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
    control_provided_refs: list[ARRef]
    service_control: Optional[Any]
    signal_service_event_propses: list[Any]
    def __init__(self) -> None:
        """Initialize SignalServiceTranslationProps."""
        super().__init__()
        self.control_refs: list[ARRef] = []
        self.control_pnc_refs: list[ARRef] = []
        self.control_provided_refs: list[ARRef] = []
        self.service_control: Optional[Any] = None
        self.signal_service_event_propses: list[Any] = []

    def serialize(self) -> ET.Element:
        """Serialize SignalServiceTranslationProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SignalServiceTranslationProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize control_refs (list to container "CONTROL-REFS")
        if self.control_refs:
            wrapper = ET.Element("CONTROL-REFS")
            for item in self.control_refs:
                serialized = SerializationHelper.serialize_item(item, "ConsumedEventGroup")
                if serialized is not None:
                    child_elem = ET.Element("CONTROL-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize control_pnc_refs (list to container "CONTROL-PNC-REFS")
        if self.control_pnc_refs:
            wrapper = ET.Element("CONTROL-PNC-REFS")
            for item in self.control_pnc_refs:
                serialized = SerializationHelper.serialize_item(item, "PncMappingIdent")
                if serialized is not None:
                    child_elem = ET.Element("CONTROL-PNC-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize control_provided_refs (list to container "CONTROL-PROVIDED-REFS")
        if self.control_provided_refs:
            wrapper = ET.Element("CONTROL-PROVIDED-REFS")
            for item in self.control_provided_refs:
                serialized = SerializationHelper.serialize_item(item, "EventHandler")
                if serialized is not None:
                    child_elem = ET.Element("CONTROL-PROVIDED-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize service_control
        if self.service_control is not None:
            serialized = SerializationHelper.serialize_item(self.service_control, "Any")
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
                serialized = SerializationHelper.serialize_item(item, "Any")
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

        # Parse control_refs (list from container "CONTROL-REFS")
        obj.control_refs = []
        container = SerializationHelper.find_child_element(element, "CONTROL-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.control_refs.append(child_value)

        # Parse control_pnc_refs (list from container "CONTROL-PNC-REFS")
        obj.control_pnc_refs = []
        container = SerializationHelper.find_child_element(element, "CONTROL-PNC-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.control_pnc_refs.append(child_value)

        # Parse control_provided_refs (list from container "CONTROL-PROVIDED-REFS")
        obj.control_provided_refs = []
        container = SerializationHelper.find_child_element(element, "CONTROL-PROVIDED-REFS")
        if container is not None:
            for child in container:
                # Check if child is a reference element (ends with -REF or -TREF)
                child_tag = SerializationHelper.strip_namespace(child.tag)
                if child_tag.endswith("-REF") or child_tag.endswith("-TREF"):
                    # Use ARRef.deserialize() for reference elements
                    child_value = ARRef.deserialize(child)
                else:
                    # Deserialize each child element dynamically based on its tag
                    child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.control_provided_refs.append(child_value)

        # Parse service_control
        child = SerializationHelper.find_child_element(element, "SERVICE-CONTROL")
        if child is not None:
            service_control_value = child.text
            obj.service_control = service_control_value

        # Parse signal_service_event_propses (list from container "SIGNAL-SERVICE-EVENT-PROPSES")
        obj.signal_service_event_propses = []
        container = SerializationHelper.find_child_element(element, "SIGNAL-SERVICE-EVENT-PROPSES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
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
