"""DataPrototypeTransformationProps AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 787)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Transformer.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel2.models.M2.builder_base import BuilderBase
from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel2.models.M2.AUTOSARTemplates.SWComponentTemplate.Datatype.DataPrototypes.data_prototype import (
    DataPrototype,
)
from armodel2.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.transformation_props import (
    TransformationProps,
)

if TYPE_CHECKING:
    from armodel2.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
        SwDataDefProps,
    )



from armodel2.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel2.serialization import SerializationHelper
class DataPrototypeTransformationProps(ARObject):
    """AUTOSAR DataPrototypeTransformationProps."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    _XML_TAG = "DATA-PROTOTYPE-TRANSFORMATION-PROPS"


    data_prototype_in_ref: Optional[ARRef]
    network: Optional[SwDataDefProps]
    transformation_props_ref: Optional[ARRef]
    _DESERIALIZE_DISPATCH = {
        "DATA-PROTOTYPE-IN-REF": ("_POLYMORPHIC", "data_prototype_in_ref", ["ApplicationArrayElement", "ApplicationCompositeElementDataPrototype", "ApplicationRecordElement", "ArgumentDataPrototype", "AutosarDataPrototype", "ParameterDataPrototype", "VariableDataPrototype"]),
        "NETWORK": lambda obj, elem: setattr(obj, "network", SerializationHelper.deserialize_by_tag(elem, "SwDataDefProps")),
        "TRANSFORMATION-PROPS-REF": ("_POLYMORPHIC", "transformation_props_ref", ["SOMEIPTransformationProps", "UserDefinedTransformationProps"]),
    }


    def __init__(self) -> None:
        """Initialize DataPrototypeTransformationProps."""
        super().__init__()
        self.data_prototype_in_ref: Optional[ARRef] = None
        self.network: Optional[SwDataDefProps] = None
        self.transformation_props_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize DataPrototypeTransformationProps to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Use pre-computed _XML_TAG constant
        elem = ET.Element(self._XML_TAG)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(DataPrototypeTransformationProps, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize data_prototype_in_ref
        if self.data_prototype_in_ref is not None:
            serialized = SerializationHelper.serialize_item(self.data_prototype_in_ref, "DataPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("DATA-PROTOTYPE-IN-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize network
        if self.network is not None:
            serialized = SerializationHelper.serialize_item(self.network, "SwDataDefProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("NETWORK")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize transformation_props_ref
        if self.transformation_props_ref is not None:
            serialized = SerializationHelper.serialize_item(self.transformation_props_ref, "TransformationProps")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSFORMATION-PROPS-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                if serialized.text:
                    wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "DataPrototypeTransformationProps":
        """Deserialize XML element to DataPrototypeTransformationProps object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized DataPrototypeTransformationProps object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(DataPrototypeTransformationProps, cls).deserialize(element)

        # Single-pass deserialization with if-elif-else chain
        ns_split = '}'
        for child in element:
            tag = child.tag.split(ns_split, 1)[1] if child.tag.startswith('{') else child.tag
            if tag == "DATA-PROTOTYPE-IN-REF":
                setattr(obj, "data_prototype_in_ref", ARRef.deserialize(child))
            elif tag == "NETWORK":
                setattr(obj, "network", SerializationHelper.deserialize_by_tag(child, "SwDataDefProps"))
            elif tag == "TRANSFORMATION-PROPS-REF":
                setattr(obj, "transformation_props_ref", ARRef.deserialize(child))

        return obj



class DataPrototypeTransformationPropsBuilder(BuilderBase):
    """Builder for DataPrototypeTransformationProps with fluent API."""

    def __init__(self) -> None:
        """Initialize builder with defaults."""
        super().__init__()
        self._obj: DataPrototypeTransformationProps = DataPrototypeTransformationProps()


    def with_data_prototype_in(self, value: Optional[DataPrototype]) -> "DataPrototypeTransformationPropsBuilder":
        """Set data_prototype_in attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'data_prototype_in' is required and cannot be None")
        self._obj.data_prototype_in = value
        return self

    def with_network(self, value: Optional[SwDataDefProps]) -> "DataPrototypeTransformationPropsBuilder":
        """Set network attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'network' is required and cannot be None")
        self._obj.network = value
        return self

    def with_transformation_props(self, value: Optional[TransformationProps]) -> "DataPrototypeTransformationPropsBuilder":
        """Set transformation_props attribute.

        Args:
            value: Value to set

        Returns:
            self for method chaining
        """
        if value is None and not True:
            raise ValueError("Attribute 'transformation_props' is required and cannot be None")
        self._obj.transformation_props = value
        return self



    # Pre-computed validation constants (generated from JSON schema)
    _OPTIONAL_ATTRIBUTES = {
        "dataPrototypeIn",
        "network",
        "transformationProps",
    }


    def _validate_instance(self) -> None:
        """Validate the built instance based on settings."""
        from armodel2.core import GlobalSettingsManager, BuilderValidationMode

        settings = GlobalSettingsManager()
        mode = settings.builder_validation

        if mode == BuilderValidationMode.DISABLED:
            return

        # No required attributes to validate (all are optional)


    def build(self) -> DataPrototypeTransformationProps:
        """Build and return the DataPrototypeTransformationProps instance with validation."""
        self._validate_instance()
        return self._obj