"""ParameterInterface AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 41)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2042)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_PortInterface.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import (
    DataInterface,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.data_interface import DataInterfaceBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.parameter_data_prototype import (
    ParameterDataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class ParameterInterface(DataInterface):
    """AUTOSAR ParameterInterface."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "PARAMETER-INTERFACE"


    parameter_refs: list[ARRef]
    _DESERIALIZE_DISPATCH = {
        "PARAMETER-REFS": lambda obj, elem: [obj.parameter_refs.append(ARRef.deserialize(item_elem)) for item_elem in elem],
    }


    def __init__(self) -> None:
        """Initialize ParameterInterface."""
        super().__init__()
        self.parameter_refs: list[ARRef] = []

    def serialize(self) -> ET.Element:
        """Serialize ParameterInterface to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(ParameterInterface, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize parameter_refs (list to container "PARAMETER-REFS")
        if self.parameter_refs:
            wrapper = ET.Element("PARAMETER-REFS")
            for item in self.parameter_refs:
                serialized = SerializationHelper.serialize_item(item, "ParameterDataPrototype")
                if serialized is not None:
                    child_elem = ET.Element("PARAMETER-REF")
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
    def deserialize(cls, element: ET.Element) -> "ParameterInterface":
        """Deserialize XML element to ParameterInterface object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized ParameterInterface object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(ParameterInterface, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "PARAMETER-REFS":
                # Iterate through wrapper children
                for item_elem in child:
                    obj.parameter_refs.append(ARRef.deserialize(item_elem))

        return obj



class ParameterInterfaceBuilder(DataInterfaceBuilder):
    """Builder for ParameterInterface with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: ParameterInterface = ParameterInterface()


    def with_parameters(self, items: list[ParameterDataPrototype]) -> "ParameterInterfaceBuilder":
        """Set parameters list attribute.

        Args:
            items: List of items to set

        Returns:
            self for method chaining
        """
        self._obj.parameters = list(items) if items else []
        return self


    def add_parameter(self, item: ParameterDataPrototype) -> "ParameterInterfaceBuilder":
        """Add a single item to parameters list.

        Args:
            item: Item to add

        Returns:
            self for method chaining
        """
        self._obj.parameters.append(item)
        return self

    def clear_parameters(self) -> "ParameterInterfaceBuilder":
        """Clear all items from parameters list.

        Returns:
            self for method chaining
        """
        self._obj.parameters = []
        return self


    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "parameter",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> ParameterInterface:
        """Build and return the ParameterInterface instance with validation."""
        self._validate_instance()
        return self._obj