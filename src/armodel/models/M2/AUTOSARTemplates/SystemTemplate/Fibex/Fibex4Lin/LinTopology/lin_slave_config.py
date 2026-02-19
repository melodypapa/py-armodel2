"""LinSlaveConfig AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SystemTemplate.pdf (page 94)

JSON Source: docs/json/packages/M2_AUTOSARTemplates_SystemTemplate_Fibex_Fibex4Lin_LinTopology.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Integer,
    PositiveInteger,
    String,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_configurable_frame import (
    LinConfigurableFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_error_response import (
    LinErrorResponse,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_ordered_configurable_frame import (
    LinOrderedConfigurableFrame,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinTopology.lin_slave_config_ident import (
    LinSlaveConfigIdent,
)


class LinSlaveConfig(ARObject):
    """AUTOSAR LinSlaveConfig."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    configured_nad: Optional[Integer]
    function_id: Optional[PositiveInteger]
    ident: Optional[LinSlaveConfigIdent]
    initial_nad: Optional[Integer]
    lin_configurable_frames: list[LinConfigurableFrame]
    lin_error_response: Optional[LinErrorResponse]
    lin_ordereds: list[LinOrderedConfigurableFrame]
    protocol_version: Optional[String]
    supplier_id: Optional[PositiveInteger]
    variant_id: Optional[PositiveInteger]
    def __init__(self) -> None:
        """Initialize LinSlaveConfig."""
        super().__init__()
        self.configured_nad: Optional[Integer] = None
        self.function_id: Optional[PositiveInteger] = None
        self.ident: Optional[LinSlaveConfigIdent] = None
        self.initial_nad: Optional[Integer] = None
        self.lin_configurable_frames: list[LinConfigurableFrame] = []
        self.lin_error_response: Optional[LinErrorResponse] = None
        self.lin_ordereds: list[LinOrderedConfigurableFrame] = []
        self.protocol_version: Optional[String] = None
        self.supplier_id: Optional[PositiveInteger] = None
        self.variant_id: Optional[PositiveInteger] = None
    def serialize(self) -> ET.Element:
        """Serialize LinSlaveConfig to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize configured_nad
        if self.configured_nad is not None:
            serialized = ARObject._serialize_item(self.configured_nad, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("CONFIGURED-NAD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize function_id
        if self.function_id is not None:
            serialized = ARObject._serialize_item(self.function_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("FUNCTION-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize ident
        if self.ident is not None:
            serialized = ARObject._serialize_item(self.ident, "LinSlaveConfigIdent")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("IDENT")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize initial_nad
        if self.initial_nad is not None:
            serialized = ARObject._serialize_item(self.initial_nad, "Integer")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("INITIAL-NAD")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lin_configurable_frames (list to container "LIN-CONFIGURABLE-FRAMES")
        if self.lin_configurable_frames:
            wrapper = ET.Element("LIN-CONFIGURABLE-FRAMES")
            for item in self.lin_configurable_frames:
                serialized = ARObject._serialize_item(item, "LinConfigurableFrame")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize lin_error_response
        if self.lin_error_response is not None:
            serialized = ARObject._serialize_item(self.lin_error_response, "LinErrorResponse")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("LIN-ERROR-RESPONSE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize lin_ordereds (list to container "LIN-ORDEREDS")
        if self.lin_ordereds:
            wrapper = ET.Element("LIN-ORDEREDS")
            for item in self.lin_ordereds:
                serialized = ARObject._serialize_item(item, "LinOrderedConfigurableFrame")
                if serialized is not None:
                    wrapper.append(serialized)
            if len(wrapper) > 0:
                elem.append(wrapper)

        # Serialize protocol_version
        if self.protocol_version is not None:
            serialized = ARObject._serialize_item(self.protocol_version, "String")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("PROTOCOL-VERSION")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize supplier_id
        if self.supplier_id is not None:
            serialized = ARObject._serialize_item(self.supplier_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SUPPLIER-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize variant_id
        if self.variant_id is not None:
            serialized = ARObject._serialize_item(self.variant_id, "PositiveInteger")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("VARIANT-ID")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "LinSlaveConfig":
        """Deserialize XML element to LinSlaveConfig object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized LinSlaveConfig object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse configured_nad
        child = ARObject._find_child_element(element, "CONFIGURED-NAD")
        if child is not None:
            configured_nad_value = child.text
            obj.configured_nad = configured_nad_value

        # Parse function_id
        child = ARObject._find_child_element(element, "FUNCTION-ID")
        if child is not None:
            function_id_value = child.text
            obj.function_id = function_id_value

        # Parse ident
        child = ARObject._find_child_element(element, "IDENT")
        if child is not None:
            ident_value = ARObject._deserialize_by_tag(child, "LinSlaveConfigIdent")
            obj.ident = ident_value

        # Parse initial_nad
        child = ARObject._find_child_element(element, "INITIAL-NAD")
        if child is not None:
            initial_nad_value = child.text
            obj.initial_nad = initial_nad_value

        # Parse lin_configurable_frames (list from container "LIN-CONFIGURABLE-FRAMES")
        obj.lin_configurable_frames = []
        container = ARObject._find_child_element(element, "LIN-CONFIGURABLE-FRAMES")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.lin_configurable_frames.append(child_value)

        # Parse lin_error_response
        child = ARObject._find_child_element(element, "LIN-ERROR-RESPONSE")
        if child is not None:
            lin_error_response_value = ARObject._deserialize_by_tag(child, "LinErrorResponse")
            obj.lin_error_response = lin_error_response_value

        # Parse lin_ordereds (list from container "LIN-ORDEREDS")
        obj.lin_ordereds = []
        container = ARObject._find_child_element(element, "LIN-ORDEREDS")
        if container is not None:
            for child in container:
                # Deserialize each child element dynamically based on its tag
                child_value = ARObject._deserialize_by_tag(child, None)
                if child_value is not None:
                    obj.lin_ordereds.append(child_value)

        # Parse protocol_version
        child = ARObject._find_child_element(element, "PROTOCOL-VERSION")
        if child is not None:
            protocol_version_value = child.text
            obj.protocol_version = protocol_version_value

        # Parse supplier_id
        child = ARObject._find_child_element(element, "SUPPLIER-ID")
        if child is not None:
            supplier_id_value = child.text
            obj.supplier_id = supplier_id_value

        # Parse variant_id
        child = ARObject._find_child_element(element, "VARIANT-ID")
        if child is not None:
            variant_id_value = child.text
            obj.variant_id = variant_id_value

        return obj



class LinSlaveConfigBuilder:
    """Builder for LinSlaveConfig."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinSlaveConfig = LinSlaveConfig()

    def build(self) -> LinSlaveConfig:
        """Build and return LinSlaveConfig object.

        Returns:
            LinSlaveConfig instance
        """
        # TODO: Add validation
        return self._obj
