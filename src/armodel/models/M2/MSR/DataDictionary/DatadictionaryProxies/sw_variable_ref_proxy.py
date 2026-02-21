"""SwVariableRefProxy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DatadictionaryProxies.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.serialization import SerializationHelper
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef

if TYPE_CHECKING:
    from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
        AutosarVariableRef,
    )
    from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
        McDataInstance,
    )



class SwVariableRefProxy(ARObject):
    """AUTOSAR SwVariableRefProxy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    autosar_variable_ref: Optional[ARRef]
    mc_data_instance_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwVariableRefProxy."""
        super().__init__()
        self.autosar_variable_ref: Optional[ARRef] = None
        self.mc_data_instance_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwVariableRefProxy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = SerializationHelper.get_xml_tag(self.__class__)
        elem = ET.Element(tag)

        # First, call parent's serialize to handle inherited attributes
        parent_elem = super(SwVariableRefProxy, self).serialize()

        # Copy all attributes from parent element
        elem.attrib.update(parent_elem.attrib)

        # Copy text from parent element
        if parent_elem.text:
            elem.text = parent_elem.text

        # Copy all children from parent element
        for child in parent_elem:
            elem.append(child)

        # Serialize autosar_variable_ref
        if self.autosar_variable_ref is not None:
            serialized = SerializationHelper.serialize_item(self.autosar_variable_ref, "AutosarVariableRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AUTOSAR-VARIABLE-REF-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mc_data_instance_ref
        if self.mc_data_instance_ref is not None:
            serialized = SerializationHelper.serialize_item(self.mc_data_instance_ref, "McDataInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MC-DATA-INSTANCE-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwVariableRefProxy":
        """Deserialize XML element to SwVariableRefProxy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwVariableRefProxy object
        """
        # First, call parent's deserialize to handle inherited attributes
        obj = super(SwVariableRefProxy, cls).deserialize(element)

        # Parse autosar_variable_ref
        child = SerializationHelper.find_child_element(element, "AUTOSAR-VARIABLE-REF-REF")
        if child is not None:
            autosar_variable_ref_value = ARRef.deserialize(child)
            obj.autosar_variable_ref = autosar_variable_ref_value

        # Parse mc_data_instance_ref
        child = SerializationHelper.find_child_element(element, "MC-DATA-INSTANCE-REF")
        if child is not None:
            mc_data_instance_ref_value = ARRef.deserialize(child)
            obj.mc_data_instance_ref = mc_data_instance_ref_value

        return obj



class SwVariableRefProxyBuilder:
    """Builder for SwVariableRefProxy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwVariableRefProxy = SwVariableRefProxy()

    def build(self) -> SwVariableRefProxy:
        """Build and return SwVariableRefProxy object.

        Returns:
            SwVariableRefProxy instance
        """
        # TODO: Add validation
        return self._obj
