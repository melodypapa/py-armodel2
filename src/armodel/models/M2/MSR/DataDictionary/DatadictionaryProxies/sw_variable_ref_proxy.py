"""SwVariableRefProxy AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.MeasurementCalibrationSupport.mc_data_instance import (
    McDataInstance,
)


class SwVariableRefProxy(ARObject):
    """AUTOSAR SwVariableRefProxy."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("autosar_variable_ref", None, False, False, AutosarVariableRef),  # autosarVariableRef
        ("mc_data_instance", None, False, False, McDataInstance),  # mcDataInstance
    ]

    def __init__(self) -> None:
        """Initialize SwVariableRefProxy."""
        super().__init__()
        self.autosar_variable_ref: Optional[AutosarVariableRef] = None
        self.mc_data_instance: Optional[McDataInstance] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert SwVariableRefProxy to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "SwVariableRefProxy":
        """Create SwVariableRefProxy from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            SwVariableRefProxy instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to SwVariableRefProxy since parent returns ARObject
        return cast("SwVariableRefProxy", obj)


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
