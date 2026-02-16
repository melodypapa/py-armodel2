"""PortPrototypeBlueprint AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ARPackage.ar_element import (
    ARElement,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.p_port_com_spec import (
    PPortComSpec,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)
from armodel.models.M2.AUTOSARTemplates.CommonStructure.StandardizationTemplate.BlueprintDedicated.Port.port_prototype_blueprint import (
    PortPrototypeBlueprint,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Communication.r_port_com_spec import (
    RPortComSpec,
)


class PortPrototypeBlueprint(ARElement):
    """AUTOSAR PortPrototypeBlueprint."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("init_values", None, False, True, PortPrototypeBlueprint),  # initValues
        ("interface", None, False, False, PortInterface),  # interface
        ("provided_coms", None, False, True, PPortComSpec),  # providedComs
        ("required_coms", None, False, True, RPortComSpec),  # requiredComs
    ]

    def __init__(self) -> None:
        """Initialize PortPrototypeBlueprint."""
        super().__init__()
        self.init_values: list[PortPrototypeBlueprint] = []
        self.interface: PortInterface = None
        self.provided_coms: list[PPortComSpec] = []
        self.required_coms: list[RPortComSpec] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert PortPrototypeBlueprint to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "PortPrototypeBlueprint":
        """Create PortPrototypeBlueprint from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            PortPrototypeBlueprint instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to PortPrototypeBlueprint since parent returns ARObject
        return cast("PortPrototypeBlueprint", obj)


class PortPrototypeBlueprintBuilder:
    """Builder for PortPrototypeBlueprint."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: PortPrototypeBlueprint = PortPrototypeBlueprint()

    def build(self) -> PortPrototypeBlueprint:
        """Build and return PortPrototypeBlueprint object.

        Returns:
            PortPrototypeBlueprint instance
        """
        # TODO: Add validation
        return self._obj
