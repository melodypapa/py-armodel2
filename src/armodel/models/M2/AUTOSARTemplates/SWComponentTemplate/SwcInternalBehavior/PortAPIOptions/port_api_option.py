"""PortAPIOption AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 589)
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 2045)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SWComponentTemplate_SwcInternalBehavior_PortAPIOptions.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Transformer.data_transformation import (
    DataTransformation,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.port_defined_argument_value import (
    PortDefinedArgumentValue,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.port_prototype import (
    PortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.PortAPIOptions.swc_supported_feature import (
    SwcSupportedFeature,
)


class PortAPIOption(ARObject):
    """AUTOSAR PortAPIOption."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    enable_take: Optional[Boolean]
    error_handling: Optional[DataTransformation]
    indirect_api: Optional[Boolean]
    port_ref: Optional[ARRef]
    port_arg_values: list[PortDefinedArgumentValue]
    supporteds: list[SwcSupportedFeature]
    transformer: Optional[DataTransformation]
    def __init__(self) -> None:
        """Initialize PortAPIOption."""
        super().__init__()
        self.enable_take: Optional[Boolean] = None
        self.error_handling: Optional[DataTransformation] = None
        self.indirect_api: Optional[Boolean] = None
        self.port_ref: Optional[ARRef] = None
        self.port_arg_values: list[PortDefinedArgumentValue] = []
        self.supporteds: list[SwcSupportedFeature] = []
        self.transformer: Optional[DataTransformation] = None

    def serialize(self) -> ET.Element:
        """Serialize PortAPIOption to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize enable_take
        if self.enable_take is not None:
            serialized = ARObject._serialize_item(self.enable_take, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ENABLE-TAKE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize error_handling
        if self.error_handling is not None:
            serialized = ARObject._serialize_item(self.error_handling, "DataTransformation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("ERROR-HANDLING")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize indirect_api
        if self.indirect_api is not None:
            serialized = ARObject._serialize_item(self.indirect_api, "Boolean")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INDIRECT-API")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize port_ref
        if self.port_ref is not None:
            serialized = ARObject._serialize_item(self.port_ref, "PortPrototype")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PORT-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize port_arg_values (list to container "PORT-ARG-VALUES")
        if self.port_arg_values:
            wrapper = ET.Element("PORT-ARG-VALUES")
            for item in self.port_arg_values:
                serialized = ARObject._serialize_item(item, "PortDefinedArgumentValue")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize supporteds (list to container "SUPPORTEDS")
        if self.supporteds:
            wrapper = ET.Element("SUPPORTEDS")
            for item in self.supporteds:
                serialized = ARObject._serialize_item(item, "SwcSupportedFeature")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize transformer
        if self.transformer is not None:
            serialized = ARObject._serialize_item(self.transformer, "DataTransformation")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("TRANSFORMER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortAPIOption":
        """Deserialize XML element to PortAPIOption object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized PortAPIOption object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse enable_take
        child = ARObject._find_child_element(element, "ENABLE-TAKE")
        if child is not None:
            enable_take_value = child.text
            obj.enable_take = enable_take_value

        # Parse error_handling
        child = ARObject._find_child_element(element, "ERROR-HANDLING")
        if child is not None:
            error_handling_value = ARObject._deserialize_by_tag(child, "DataTransformation")
            obj.error_handling = error_handling_value

        # Parse indirect_api
        child = ARObject._find_child_element(element, "INDIRECT-API")
        if child is not None:
            indirect_api_value = child.text
            obj.indirect_api = indirect_api_value

        # Parse port_ref
        child = ARObject._find_child_element(element, "PORT-REF")
        if child is not None:
            port_ref_value = ARRef.deserialize(child)
            obj.port_ref = port_ref_value

        # Parse port_arg_values (list from container "PORT-ARG-VALUES")
        obj.port_arg_values = []
        container = ARObject._find_child_element(element, "PORT-ARG-VALUES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.port_arg_values.append(child_value)

        # Parse supporteds (list from container "SUPPORTEDS")
        obj.supporteds = []
        container = ARObject._find_child_element(element, "SUPPORTEDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.supporteds.append(child_value)

        # Parse transformer
        child = ARObject._find_child_element(element, "TRANSFORMER")
        if child is not None:
            transformer_value = ARObject._deserialize_by_tag(child, "DataTransformation")
            obj.transformer = transformer_value

        return obj



class PortAPIOptionBuilder:
    """Builder for PortAPIOption."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortAPIOption = PortAPIOption()

    def build(self) -> PortAPIOption:
        """Build and return PortAPIOption object.

        Returns:
            PortAPIOption instance
        """
        # TODO: Add validation
        return self._obj
