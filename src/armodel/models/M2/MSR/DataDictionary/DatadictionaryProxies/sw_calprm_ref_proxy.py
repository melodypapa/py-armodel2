"""SwCalprmRefProxy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
    AutosarParameterRef,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)


class SwCalprmRefProxy(ARObject):
    """AUTOSAR SwCalprmRefProxy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ar_parameter", None, False, False, AutosarParameterRef),  # arParameter
        ("mc_data_instance", None, False, False, McDataInstance),  # mcDataInstance
    ]

    def __init__(self) -> None:
        """Initialize SwCalprmRefProxy."""
        super().__init__()
        self.ar_parameter: Optional[AutosarParameterRef] = None
        self.mc_data_instance: Optional[McDataInstance] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwCalprmRefProxy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwCalprmRefProxy":
        """Create SwCalprmRefProxy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwCalprmRefProxy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwCalprmRefProxy since parent returns ARObject
        return cast("SwCalprmRefProxy", obj)


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
