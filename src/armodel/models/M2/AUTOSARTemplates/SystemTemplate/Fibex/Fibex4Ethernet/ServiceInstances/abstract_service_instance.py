"""AbstractServiceInstance AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 476)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Ethernet_ServiceInstances.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ServiceInstances.pdu_activation_routing_group import (
    PduActivationRoutingGroup,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Ethernet.ObsoleteModel.so_ad_routing_group import (
    SoAdRoutingGroup,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.TagWithOptionalValue.tag_with_optional_value import (
    TagWithOptionalValue,
)
from abc import ABC, abstractmethod


class AbstractServiceInstance(Identifiable, ABC):
    """AUTOSAR AbstractServiceInstance."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    capabilities: list[TagWithOptionalValue]
    major_version: Optional[PositiveInteger]
    method: Optional[PduActivationRoutingGroup]
    routing_group_refs: list[ARRef]
    def __init__(self) -> None:
        """Initialize AbstractServiceInstance."""
        super().__init__()
        self.capabilities: list[TagWithOptionalValue] = []
        self.major_version: Optional[PositiveInteger] = None
        self.method: Optional[PduActivationRoutingGroup] = None
        self.routing_group_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize AbstractServiceInstance to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractServiceInstance, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize capabilities (list to container "CAPABILITIES")
        if self.capabilities:
            wrapper = ET.Element("CAPABILITIES")
            for item in self.capabilities:
                serialized = SerializationHelper.serialize_item(item, "TagWithOptionalValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize major_version
        if self.major_version is not None:
            serialized = SerializationHelper.serialize_item(self.major_version, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MAJOR-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize method
        if self.method is not None:
            serialized = SerializationHelper.serialize_item(self.method, "PduActivationRoutingGroup")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("METHOD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize routing_group_refs (list to container "ROUTING-GROUP-REFS")
        if self.routing_group_refs:
            wrapper = ET.Element("ROUTING-GROUP-REFS")
            for item in self.routing_group_refs:
                serialized = SerializationHelper.serialize_item(item, "SoAdRoutingGroup")
                if serialized is not None:
                    child_elem = ET.Element("ROUTING-GROUP-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractServiceInstance":
        """Deserialize XML element to AbstractServiceInstance object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractServiceInstance object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractServiceInstance, cls).deserialize(element)

        # Parse capabilities (list from container "CAPABILITIES")
        obj.capabilities = []
        container = SerializationHelper.find_child_element(element, "CAPABILITIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.capabilities.append(child_value)

        # Parse major_version
        child = SerializationHelper.find_child_element(element, "MAJOR-VERSION")
        if child is not None:
            major_version_value = child.text
            obj.major_version = major_version_value

        # Parse method
        child = SerializationHelper.find_child_element(element, "METHOD")
        if child is not None:
            method_value = SerializationHelper.deserialize_by_tag(child, "PduActivationRoutingGroup")
            obj.method = method_value

        # Parse routing_group_refs (list from container "ROUTING-GROUP-REFS")
        obj.routing_group_refs = []
        container = SerializationHelper.find_child_element(element, "ROUTING-GROUP-REFS")
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
                    obj.routing_group_refs.append(child_value)

        return obj



