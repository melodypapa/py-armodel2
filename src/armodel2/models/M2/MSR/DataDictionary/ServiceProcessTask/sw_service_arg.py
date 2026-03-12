"""SwServiceArg AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_BSWModuleDescriptionTemplate.pdf (page 38)
  - AUTOSAR_CP_TPS_ECUConfiguration.pdf (page 312)
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 1006)
  - AUTOSAR_FO_TPS_GenericStructureTemplate.pdf (page 472)
  - AUTOSAR_FO_TPS_StandardizationTemplate.pdf (page 215)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_ServiceProcessTask.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import (
    Identifiable,
)
from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.Identifiable.identifiable import IdentifiableBuilder
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    ArgumentDirectionEnum,
)
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Numerical,
)
from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.value_list import (
    ValueList,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class SwServiceArg(Identifiable):
    """AUTOSAR SwServiceArg."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "SW-SERVICE-ARG"


    direction: Optional[ArgumentDirectionEnum]
    sw_arraysize: Optional[ValueList]
    v: Optional[Numerical]
    sw_data_def_props: Optional[SwDataDefProps]
    _DESERIALIZE_DISPATCH = {
        "DIRECTION": lambda obj, elem: setattr(obj, "direction", ArgumentDirectionEnum.deserialize(elem)),
        "SW-ARRAYSIZE": lambda obj, elem: setattr(obj, "sw_arraysize", SerializationHelper.deserialize_by_tag(elem, "ValueList")),
        "V": lambda obj, elem: setattr(obj, "v", SerializationHelper.deserialize_by_tag(elem, "Numerical")),
        "SW-DATA-DEF-PROPS": lambda obj, elem: setattr(obj, "sw_data_def_props", SerializationHelper.deserialize_by_tag(elem, "SwDataDefProps")),
    }


    def __init__(self) -> None:
        """Initialize SwServiceArg."""
        super().__init__()
        self.direction: Optional[ArgumentDirectionEnum] = None
        self.sw_arraysize: Optional[ValueList] = None
        self.v: Optional[Numerical] = None
        self.sw_data_def_props: Optional[SwDataDefProps] = None

    def serialize(self) -> ET.Element:
        """Serialize SwServiceArg to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwServiceArg, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize direction
        if self.direction is not None:
            serialized = SerializationHelper.serialize_item(self.direction, "ArgumentDirectionEnum")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DIRECTION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_arraysize (atp_mixed - append children directly)
        if self.sw_arraysize is not None:
            serialized = SerializationHelper.serialize_item(self.sw_arraysize, "ValueList")
            if serialized is not None:
                # atpMixed type: append children directly without wrapper
                if hasattr(serialized, 'attrib'):
                    elem.attrib.update(serialized.attrib)
                # Only copy text if it's a non-empty string (not None or whitespace)
                if serialized.text and serialized.text.strip():
                    elem.text = serialized.text
                for child in serialized:
                    elem.append(child)

        # Serialize v
        if self.v is not None:
            serialized = SerializationHelper.serialize_item(self.v, "Numerical")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("V")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_data_def_props
        if self.sw_data_def_props is not None:
            serialized = SerializationHelper.serialize_item(self.sw_data_def_props, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-DATA-DEF-PROPS")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwServiceArg":
        """Deserialize XML element to SwServiceArg object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwServiceArg object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwServiceArg, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DIRECTION":
                setattr(obj, "direction", ArgumentDirectionEnum.deserialize(child))
            elif tag == "SW-ARRAYSIZE":
                setattr(obj, "sw_arraysize", SerializationHelper.deserialize_by_tag(child, "ValueList"))
            elif tag == "V":
                setattr(obj, "v", SerializationHelper.deserialize_by_tag(child, "Numerical"))
            elif tag == "SW-DATA-DEF-PROPS":
                setattr(obj, "sw_data_def_props", SerializationHelper.deserialize_by_tag(child, "SwDataDefProps"))

        return obj



class SwServiceArgBuilder(IdentifiableBuilder):
    """Builder for SwServiceArg with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: SwServiceArg = SwServiceArg()


    def with_direction(self, value: Optional[ArgumentDirectionEnum]) -> "SwServiceArgBuilder":
        """Set direction attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'direction' is required and cannot be None")
        self._obj.direction = value
        return self

    def with_sw_arraysize(self, value: Optional[ValueList]) -> "SwServiceArgBuilder":
        """Set sw_arraysize attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_arraysize' is required and cannot be None")
        self._obj.sw_arraysize = value
        return self

    def with_v(self, value: Optional[Numerical]) -> "SwServiceArgBuilder":
        """Set v attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'v' is required and cannot be None")
        self._obj.v = value
        return self

    def with_sw_data_def_props(self, value: Optional[SwDataDefProps]) -> "SwServiceArgBuilder":
        """Set sw_data_def_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'sw_data_def_props' is required and cannot be None")
        self._obj.sw_data_def_props = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "direction",
        "swArraysize",
        "swDataDefProps",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> SwServiceArg:
        """Build and return the SwServiceArg instance with validation."""
        self._validate_instance()
        return self._obj