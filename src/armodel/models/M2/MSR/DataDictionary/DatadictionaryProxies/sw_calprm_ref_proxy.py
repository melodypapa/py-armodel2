"""SwCalprmRefProxy AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 370)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DatadictionaryProxies.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
    AutosarParameterRef,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)


class SwCalprmRefProxy(ARObject):
    """AUTOSAR SwCalprmRefProxy."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    ar_parameter_ref: Optional[ARRef]
    mc_data_instance: Optional[McDataInstance]
    def __init__(self) -> None:
        """Initialize SwCalprmRefProxy."""
        super().__init__()
        self.ar_parameter_ref: Optional[ARRef] = None
        self.mc_data_instance: Optional[McDataInstance] = None
    def serialize(self) -> ET.Element:
        """Serialize SwCalprmRefProxy to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = ARObject._get_xml_tag(self)
        elem = ET.Element(tag)

        # Serialize ar_parameter_ref
        if self.ar_parameter_ref is not None:
            serialized = ARObject._serialize_item(self.ar_parameter_ref, "AutosarParameterRef")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("AR-PARAMETER")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize mc_data_instance
        if self.mc_data_instance is not None:
            serialized = ARObject._serialize_item(self.mc_data_instance, "McDataInstance")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("MC-DATA-INSTANCE")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwCalprmRefProxy":
        """Deserialize XML element to SwCalprmRefProxy object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwCalprmRefProxy object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse ar_parameter_ref
        child = ARObject._find_child_element(element, "AR-PARAMETER")
        if child is not None:
            ar_parameter_ref_value = ARObject._deserialize_by_tag(child, "AutosarParameterRef")
            obj.ar_parameter_ref = ar_parameter_ref_value

        # Parse mc_data_instance
        child = ARObject._find_child_element(element, "MC-DATA-INSTANCE")
        if child is not None:
            mc_data_instance_value = ARObject._deserialize_by_tag(child, "McDataInstance")
            obj.mc_data_instance = mc_data_instance_value

        return obj



class SwCalprmRefProxyBuilder:
    """Builder for SwCalprmRefProxy."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwCalprmRefProxy = SwCalprmRefProxy()

    def build(self) -> SwCalprmRefProxy:
        """Build and return SwCalprmRefProxy object.

        Returns:
            SwCalprmRefProxy instance
        """
        # TODO: Add validation
        return self._obj
