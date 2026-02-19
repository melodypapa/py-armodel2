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

    destination_uris: list[EcucDestinationUriDef]
    multiplicities: list[EcucMultiplicityConfigurationClass]
    origin: Optional[String]
    post_build_variant: Optional[Boolean]
    requires_index: Optional[Boolean]
    def __init__(self) -> None:
        """Initialize EcucContainerDef."""
        super().__init__()
        self.destination_uris: list[EcucDestinationUriDef] = []
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
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(EcucContainerDef, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize destination_uris (list to container "DESTINATION-URIS")
        if self.destination_uris:
            wrapper = ET.Element("DESTINATION-URIS")
            for item in self.destination_uris:
                serialized = ARObject._serialize_item(item, "EcucDestinationUriDef")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize multiplicities (list to container "MULTIPLICITIES")
        if self.multiplicities:
            wrapper = ET.Element("MULTIPLICITIES")
            for item in self.multiplicities:
                serialized = ARObject._serialize_item(item, "EcucMultiplicityConfigurationClass")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize origin
        if self.origin is not None:
            serialized = ARObject._serialize_item(self.origin, "String")
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
            serialized = ARObject._serialize_item(self.post_build_variant, "Boolean")
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
            serialized = ARObject._serialize_item(self.requires_index, "Boolean")
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

        # Parse destination_uris (list from container "DESTINATION-URIS")
        obj.destination_uris = []
        container = ARObject._find_child_element(element, "DESTINATION-URIS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.destination_uris.append(child_value)

        # Parse multiplicities (list from container "MULTIPLICITIES")
        obj.multiplicities = []
        container = ARObject._find_child_element(element, "MULTIPLICITIES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.multiplicities.append(child_value)

        # Parse origin
        child = ARObject._find_child_element(element, "ORIGIN")
        if child is not None:
            origin_value = child.text
            obj.origin = origin_value

        # Parse post_build_variant
        child = ARObject._find_child_element(element, "POST-BUILD-VARIANT")
        if child is not None:
            post_build_variant_value = child.text
            obj.post_build_variant = post_build_variant_value

        # Parse requires_index
        child = ARObject._find_child_element(element, "REQUIRES-INDEX")
        if child is not None:
            requires_index_value = child.text
            obj.requires_index = requires_index_value

        return obj



class EcucContainerDefBuilder:
    """Builder for EcucContainerDef."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: EcucContainerDef = EcucContainerDef()

    def build(self) -> EcucContainerDef:
        """Build and return EcucContainerDef object.

        Returns:
            EcucContainerDef instance
        """
        # TODO: Add validation
        return self._obj
