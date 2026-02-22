"""EcucContainerDef AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 36)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2020)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 184)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_ECUCParameterDefTemplate.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_definition_element import (
    EcucDefinitionElement,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
    String,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_destination_uri_def import (
    EcucDestinationUriDef,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_multiplicity_configuration_class import (
    EcucMultiplicityConfigurationClass,
)
from abc import ABC, abstractmethod


class EcucContainerDef(EcucDefinitionElement, ABC):
    """AUTOSAR EcucContainerDef."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    destination_uri_refs: list[ARRef]
    multiplicities: list[EcucMultiplicityConfigurationClass]
    origin: Optional[String]
    post_build_variant: Optional[Boolean]
    requires_index: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucContainerDef."""
        super().__init__()
        self.destination_uri_refs: list[ARRef] = []
        self.multiplicities: list[EcucMultiplicityConfigurationClass] = []
        self.origin: Optional[String] = None
        self.post_build_variant: Optional[Boolean] = None
        self.requires_index: Optional[Boolean] = None

    def serialize(self) -> ET.Element:
        """Serialize EcucContainerDef to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucContainerDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_uri_refs (list to container "DESTINATION-URI-REFS")
        if self.destination_uri_refs:
            wrapper = ET.Element("DESTINATION-URI-REFS")
            for item in self.destination_uri_refs:
                serialized = SerializationHelper.serialize_item(item, "EcucDestinationUriDef")
                if serialized is not None:
                    child_elem = ET.Element("DESTINATION-URI-REF")
                    if hasattr(serialized, 'attrib'):
                        child_elem.attrib.update(serialized.attrib)
                    if serialized.text:
                        child_elem.text = serialized.text
                    for child in serialized:
                        child_elem.append(child)
                    wrapper.append(child_elem)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize multiplicities (list to container "MULTIPLICITIES")
        if self.multiplicities:
            wrapper = ET.Element("MULTIPLICITIES")
            for item in self.multiplicities:
                serialized = SerializationHelper.serialize_item(item, "EcucMultiplicityConfigurationClass")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize origin
        if self.origin is not None:
            serialized = SerializationHelper.serialize_item(self.origin, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ORIGIN")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize post_build_variant
        if self.post_build_variant is not None:
            serialized = SerializationHelper.serialize_item(self.post_build_variant, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("POST-BUILD-VARIANT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize requires_index
        if self.requires_index is not None:
            serialized = SerializationHelper.serialize_item(self.requires_index, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("REQUIRES-INDEX")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "EcucContainerDef":
        """Deserialize XML element to EcucContainerDef object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized EcucContainerDef object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(EcucContainerDef, cls).deserialize(element)

        # Parse destination_uri_refs (list from container "DESTINATION-URI-REFS")
        obj.destination_uri_refs = []
        container = SerializationHelper.find_child_element(element, "DESTINATION-URI-REFS")
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
                    obj.destination_uri_refs.append(child_value)

        # Parse multiplicities (list from container "MULTIPLICITIES")
        obj.multiplicities = []
        container = SerializationHelper.find_child_element(element, "MULTIPLICITIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = SerializationHelper.deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.multiplicities.append(child_value)

        # Parse origin
        child = SerializationHelper.find_child_element(element, "ORIGIN")
        if child is not None:
            origin_value = child.text
            obj.origin = origin_value

        # Parse post_build_variant
        child = SerializationHelper.find_child_element(element, "POST-BUILD-VARIANT")
        if child is not None:
            post_build_variant_value = child.text
            obj.post_build_variant = post_build_variant_value

        # Parse requires_index
        child = SerializationHelper.find_child_element(element, "REQUIRES-INDEX")
        if child is not None:
            requires_index_value = child.text
            obj.requires_index = requires_index_value

        return obj



