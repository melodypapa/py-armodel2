"""SwDataDependencyArgs AUTOSAR element.

References:
  - AUTOSAR_CP_TPS_SoftwareComponentTemplate.pdf (page 374)

JSON Source: docs/json/packages/M2_MSR_DataDictionary_DataDefProperties.classes.json"""

from __future__ import annotations
from typing import TYPE_CHECKING, Optional
import xml.etree.ElementTree as ET

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ArObject.ar_ref import ARRef
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_calprm_ref_proxy import (
    SwCalprmRefProxy,
)
from armodel.models.M2.MSR.DataDictionary.DatadictionaryProxies.sw_variable_ref_proxy import (
    SwVariableRefProxy,
)


class SwDataDependencyArgs(ARObject):
    """AUTOSAR SwDataDependencyArgs."""

    @property
    def is_abstract(self) -> bool:
        """Check if this class is abstract.

        Returns:
            False for concrete classes
        """
        return False

    sw_calprm_ref_proxy_ref: Optional[ARRef]
    sw_variable_ref_proxy_ref: Optional[ARRef]
    def __init__(self) -> None:
        """Initialize SwDataDependencyArgs."""
        super().__init__()
        self.sw_calprm_ref_proxy_ref: Optional[ARRef] = None
        self.sw_variable_ref_proxy_ref: Optional[ARRef] = None

    def serialize(self) -> ET.Element:
        """Serialize SwDataDependencyArgs to XML element.

        Returns:
            xml.etree.ElementTree.Element representing this object
        """
        # Get XML tag name for this class
        tag = self._get_xml_tag()
        elem = ET.Element(tag)

        # Serialize sw_calprm_ref_proxy_ref
        if self.sw_calprm_ref_proxy_ref is not None:
            serialized = ARObject._serialize_item(self.sw_calprm_ref_proxy_ref, "SwCalprmRefProxy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-CALPRM-REF-PROXY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        # Serialize sw_variable_ref_proxy_ref
        if self.sw_variable_ref_proxy_ref is not None:
            serialized = ARObject._serialize_item(self.sw_variable_ref_proxy_ref, "SwVariableRefProxy")
            if serialized is not None:
                # Wrap with correct tag
                wrapped = ET.Element("SW-VARIABLE-REF-PROXY-REF")
                if hasattr(serialized, 'attrib'):
                    wrapped.attrib.update(serialized.attrib)
                    if serialized.text:
                        wrapped.text = serialized.text
                for child in serialized:
                    wrapped.append(child)
                elem.append(wrapped)

        return elem

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwDataDependencyArgs":
        """Deserialize XML element to SwDataDependencyArgs object.

        Args:
            element: XML element to deserialize from

        Returns:
            Deserialized SwDataDependencyArgs object
        """
        # Create instance and initialize with default values
        obj = cls.__new__(cls)
        obj.__init__()

        # Parse sw_calprm_ref_proxy_ref
        child = ARObject._find_child_element(element, "SW-CALPRM-REF-PROXY-REF")
        if child is not None:
            sw_calprm_ref_proxy_ref_value = ARRef.deserialize(child)
            obj.sw_calprm_ref_proxy_ref = sw_calprm_ref_proxy_ref_value

        # Parse sw_variable_ref_proxy_ref
        child = ARObject._find_child_element(element, "SW-VARIABLE-REF-PROXY-REF")
        if child is not None:
            sw_variable_ref_proxy_ref_value = ARRef.deserialize(child)
            obj.sw_variable_ref_proxy_ref = sw_variable_ref_proxy_ref_value

        return obj



class SwDataDependencyArgsBuilder:
    """Builder for SwDataDependencyArgs."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: SwDataDependencyArgs = SwDataDependencyArgs()

    def build(self) -> SwDataDependencyArgs:
        """Build and return SwDataDependencyArgs object.

        Returns:
            SwDataDependencyArgs instance
        """
        # TODO: Add validation
        return self._obj
