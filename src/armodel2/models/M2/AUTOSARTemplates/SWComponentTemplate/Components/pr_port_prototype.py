"""PRPortPrototype AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 325)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 68)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2042)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 199)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_Components.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import AbstractRequiredPortPrototypeBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class PRPortPrototype(AbstractRequiredPortPrototype):
    """AUTOSAR PRPortPrototype."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "P-R-PORT-PROTOTYPE"


    provided_required_interface_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "PROVIDED-REQUIRED-INTERFACE-TREF": ("_POLYMORPHIC", "provided_required_interface_ref", ["ClientServerInterface", "DataInterface", "ModeSwitchInterface", "NvDataInterface", "ParameterInterface", "SenderReceiverInterface", "TriggerInterface"]),
    }


    def __init__(self) -> None:
        """Initialize PRPortPrototype."""
        super().__init__()
        self.provided_required_interface_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize PRPortPrototype to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(PRPortPrototype, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize provided_required_interface_ref
        if self.provided_required_interface_ref is not None:
            serialized = SerializationHelper.serialize_item(self.provided_required_interface_ref, "PortInterface")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROVIDED-REQUIRED-INTERFACE-TREF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PRPortPrototype":
        """Deserialize XML element to PRPortPrototype object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PRPortPrototype object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(PRPortPrototype, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PROVIDED-REQUIRED-INTERFACE-TREF":
                setattr(obj, "provided_required_interface_ref", ARRef.deserialize(child))

        return obj



class PRPortPrototypeBuilder(AbstractRequiredPortPrototypeBuilder):
    """Builder for PRPortPrototype with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: PRPortPrototype = PRPortPrototype()


    def with_provided_required_interface(self, value: Optional[PortInterface]) -> "PRPortPrototypeBuilder":
        """Set provided_required_interface attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'provided_required_interface' is required and cannot be None")
        self._obj.provided_required_interface = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "providedRequiredInterface",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> PRPortPrototype:
        """Build and return the PRPortPrototype instance with validation."""
        self._validate_instance()
        return self._obj