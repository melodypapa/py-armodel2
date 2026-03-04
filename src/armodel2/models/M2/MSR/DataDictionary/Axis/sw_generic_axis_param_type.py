"""SwGenericAxisParamType AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 356)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_Axis.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.MSR.AsamHdo.Constraints.GlobalConstraints.data_constr import (
    DataConstr,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper


class SwGenericAxisParamType(Identifiable):
    """AUTOSAR SwGenericAxisParamType."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-GENERIC-AXIS-PARAM-TYPE"


    data_constr_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DATA-CONSTR-REF": lambda obj, elem: setattr(obj, "data_constr_ref", ARRef.deserialize(elem)),
    }


    def __init__(self) -> None:
        """Initialize SwGenericAxisParamType."""
        super().__init__()
        self.data_constr_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwGenericAxisParamType to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwGenericAxisParamType, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_constr_ref
        if self.data_constr_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_constr_ref, "DataConstr")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-CONSTR-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwGenericAxisParamType":
        """Deserialize XML element to SwGenericAxisParamType object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwGenericAxisParamType object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwGenericAxisParamType, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-CONSTR-REF":
                setattr(obj, "data_constr_ref", ARRef.deserialize(child))

        return obj



class SwGenericAxisParamTypeBuilder(IdentifiableBuilder):
    """Builder for SwGenericAxisParamType with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwGenericAxisParamType = SwGenericAxisParamType()


    def with_data_constr(self, value: Optional[DataConstr]) -> "SwGenericAxisParamTypeBuilder":
        """Set data_constr attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute '" + snake_attr_name + "' is required and cannot be None")
        self._obj.data_constr = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataConstr",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwGenericAxisParamType:
        """Build and return the SwGenericAxisParamType instance with validation."""
        self._validate_instance()
        return self._obj