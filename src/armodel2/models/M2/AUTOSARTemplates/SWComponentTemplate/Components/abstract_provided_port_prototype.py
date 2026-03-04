"""AbstractProvidedPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 67)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import PortPrototypeBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AbstractProvidedPortPrototype(PortPrototype, ABC):
    """AUTOSAR AbstractProvidedPortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    provided_com_specs: list[PPortComSpec]
    _DESERIALIZE_DISPATCH = {
        "PROVIDED-COM-SPECS": ("_POLYMORPHIC_LIST", "provided_com_specs", ["ModeSwitchSenderComSpec", "NonqueuedSenderComSpec", "NvProvideComSpec", "ParameterProvideComSpec", "QueuedSenderComSpec", "SenderComSpec", "ServerComSpec"]),
    }


    def __init__(self) -> None:
        """Initialize AbstractProvidedPortPrototype."""
        super().__init__()
        self.provided_com_specs: list[PPortComSpec] = []

    def serialize(self) -> ET.Element:
        """Serialize AbstractProvidedPortPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractProvidedPortPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provided_com_specs (list to container "PROVIDED-COM-SPECS")
        if self.provided_com_specs:
            wrapper = ET.Element("PROVIDED-COM-SPECS")
            for item in self.provided_com_specs:
                serialized = SerializationHelper.serialize_item(item, "PPortComSpec")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractProvidedPortPrototype":
        """Deserialize XML element to AbstractProvidedPortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractProvidedPortPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractProvidedPortPrototype, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PROVIDED-COM-SPECS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "MODE-SWITCH-SENDER-COM-SPEC":
                        obj.provided_com_specs.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeSwitchSenderComSpec"))
                    elif concrete_tag == "NONQUEUED-SENDER-COM-SPEC":
                        obj.provided_com_specs.append(SerializationHelper.deserialize_by_tag(item_elem, "NonqueuedSenderComSpec"))
                    elif concrete_tag == "NV-PROVIDE-COM-SPEC":
                        obj.provided_com_specs.append(SerializationHelper.deserialize_by_tag(item_elem, "NvProvideComSpec"))
                    elif concrete_tag == "PARAMETER-PROVIDE-COM-SPEC":
                        obj.provided_com_specs.append(SerializationHelper.deserialize_by_tag(item_elem, "ParameterProvideComSpec"))
                    elif concrete_tag == "QUEUED-SENDER-COM-SPEC":
                        obj.provided_com_specs.append(SerializationHelper.deserialize_by_tag(item_elem, "QueuedSenderComSpec"))
                    elif concrete_tag == "SENDER-COM-SPEC":
                        obj.provided_com_specs.append(SerializationHelper.deserialize_by_tag(item_elem, "SenderComSpec"))
                    elif concrete_tag == "SERVER-COM-SPEC":
                        obj.provided_com_specs.append(SerializationHelper.deserialize_by_tag(item_elem, "ServerComSpec"))

        return obj



class AbstractProvidedPortPrototypeBuilder(PortPrototypeBuilder):
    """Builder for AbstractProvidedPortPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AbstractProvidedPortPrototype = AbstractProvidedPortPrototype()


    def with_provided_com_specs(self, items: list[PPortComSpec]) -> "AbstractProvidedPortPrototypeBuilder":
        """Set provided_com_specs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.provided_com_specs = list(items) if items else []
        return self


    def add_provided_com_spec(self, item: PPortComSpec) -> "AbstractProvidedPortPrototypeBuilder":
        """Add a single item to provided_com_specs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.provided_com_specs.append(item)
        return self

    def clear_provided_com_specs(self) -> "AbstractProvidedPortPrototypeBuilder":
        """Clear all items from provided_com_specs list.

        Returns:
            self for method chaining
        """
        self._obj.provided_com_specs = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "providedComSpec",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    @abstractmethod
    def build(self) -> AbstractProvidedPortPrototype:
        """Build and return the AbstractProvidedPortPrototype instance (abstract)."""
        raise NotImplementedError