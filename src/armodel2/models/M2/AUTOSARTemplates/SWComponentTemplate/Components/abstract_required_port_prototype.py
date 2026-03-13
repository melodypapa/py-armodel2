"""AbstractRequiredPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 67)
  - AUTOSAR_CP_TPS_TimingExtensions.pdf (page 204)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 422)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET
from armodel2.serialization.decorators import polymorphic

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import PortPrototypeBuilder
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)
from abc import ABC, abstractmethod
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class AbstractRequiredPortPrototype(PortPrototype, ABC):
    """AUTOSAR AbstractRequiredPortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            True for abstract classes
        """
        return True

    _required_com_specs: list[RPortComSpec]
    _DESERIALIZE_DISPATCH = {
        "REQUIRED-COM-SPECS": ("_POLYMORPHIC_LIST", "_required_com_specs", ["ClientComSpec", "ModeSwitchReceiverComSpec", "NonqueuedReceiverComSpec", "NvRequireComSpec", "ParameterRequireComSpec", "QueuedReceiverComSpec"]),
    }


    def __init__(self) -> None:
        """Initialize AbstractRequiredPortPrototype."""
        super().__init__()
        self._required_com_specs: list[RPortComSpec] = []
    @property
    @polymorphic({"REQUIRED-COM-SPECS": "RPortComSpec"})
    def required_com_specs(self) -> list[RPortComSpec]:
        """Get required_com_specs with polymorphic wrapper handling."""
        return self._required_com_specs

    @required_com_specs.setter
    def required_com_specs(self, value: list[RPortComSpec]) -> None:
        """Set required_com_specs with polymorphic wrapper handling."""
        self._required_com_specs = value


    def serialize(self) -> ET.Element:
        """Serialize AbstractRequiredPortPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(AbstractRequiredPortPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize required_com_specs (list with polymorphic wrapper "REQUIRED-COM-SPECS")
        if self.required_com_specs:
            container = ET.Element("REQUIRED-COM-SPECS")
            for item in self.required_com_specs:
                serialized = SerializationHelper.serialize_item(item, "RPortComSpec")
                if serialized is not None:
                    container.append(serialized)
            elem.append(container)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "AbstractRequiredPortPrototype":
        """Deserialize XML element to AbstractRequiredPortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized AbstractRequiredPortPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(AbstractRequiredPortPrototype, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "REQUIRED-COM-SPECS":
                # Iterate through all child elements and deserialize each based on its concrete type
                for item_elem in child:
                    concrete_tag = item_elem.tag.split(ns_split, 1)[1] if item_elem.tag.startswith("{") else item_elem.tag
                    if concrete_tag == "CLIENT-COM-SPEC":
                        obj._required_com_specs.append(SerializationHelper.deserialize_by_tag(item_elem, "ClientComSpec"))
                    elif concrete_tag == "MODE-SWITCH-RECEIVER-COM-SPEC":
                        obj._required_com_specs.append(SerializationHelper.deserialize_by_tag(item_elem, "ModeSwitchReceiverComSpec"))
                    elif concrete_tag == "NONQUEUED-RECEIVER-COM-SPEC":
                        obj._required_com_specs.append(SerializationHelper.deserialize_by_tag(item_elem, "NonqueuedReceiverComSpec"))
                    elif concrete_tag == "NV-REQUIRE-COM-SPEC":
                        obj._required_com_specs.append(SerializationHelper.deserialize_by_tag(item_elem, "NvRequireComSpec"))
                    elif concrete_tag == "PARAMETER-REQUIRE-COM-SPEC":
                        obj._required_com_specs.append(SerializationHelper.deserialize_by_tag(item_elem, "ParameterRequireComSpec"))
                    elif concrete_tag == "QUEUED-RECEIVER-COM-SPEC":
                        obj._required_com_specs.append(SerializationHelper.deserialize_by_tag(item_elem, "QueuedReceiverComSpec"))

        return obj



class AbstractRequiredPortPrototypeBuilder(PortPrototypeBuilder):
    """Builder for AbstractRequiredPortPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: AbstractRequiredPortPrototype = AbstractRequiredPortPrototype()


    def with_required_com_specs(self, items: list[RPortComSpec]) -> "AbstractRequiredPortPrototypeBuilder":
        """Set required_com_specs list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.required_com_specs = list(items) if items else []
        return self


    def add_required_com_spec(self, item: RPortComSpec) -> "AbstractRequiredPortPrototypeBuilder":
        """Add a single item to required_com_specs list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.required_com_specs.append(item)
        return self

    def clear_required_com_specs(self) -> "AbstractRequiredPortPrototypeBuilder":
        """Clear all items from required_com_specs list.

        Returns:
            self for method chaining
        """
        self._obj.required_com_specs = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "requiredComSpec",
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
    def build(self) -> AbstractRequiredPortPrototype:
        """Build and return the AbstractRequiredPortPrototype instance (abstract)."""
        raise NotImplementedError