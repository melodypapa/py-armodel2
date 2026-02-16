"""InstantiationDataDefProps AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_parameter_ref import (
    AutosarParameterRef,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.SwcInternalBehavior.DataElements.autosar_variable_ref import (
    AutosarVariableRef,
)
from armodel.models.M2.MSR.DataDictionary.DataDefProperties.sw_data_def_props import (
    SwDataDefProps,
)


class InstantiationDataDefProps(ARObject):
    """AUTOSAR InstantiationDataDefProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("parameter", None, False, False, AutosarParameterRef),  # parameter
        ("sw_data_def", None, False, False, SwDataDefProps),  # swDataDef
        ("variable_instance", None, False, False, AutosarVariableRef),  # variableInstance
    ]

    def __init__(self) -> None:
        """Initialize InstantiationDataDefProps."""
        super().__init__()
        self.parameter: Optional[AutosarParameterRef] = None
        self.sw_data_def: Optional[SwDataDefProps] = None
        self.variable_instance: Optional[AutosarVariableRef] = None

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert InstantiationDataDefProps to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "InstantiationDataDefProps":
        """Create InstantiationDataDefProps from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            InstantiationDataDefProps instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to InstantiationDataDefProps since parent returns ARObject
        return cast("InstantiationDataDefProps", obj)


class InstantiationDataDefPropsBuilder:
    """Builder for InstantiationDataDefProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: InstantiationDataDefProps = InstantiationDataDefProps()

    def build(self) -> InstantiationDataDefProps:
        """Build and return InstantiationDataDefProps object.

        Returns:
            InstantiationDataDefProps instance
        """
        # TODO: Add validation
        return self._obj
