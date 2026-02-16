"""BswImplementation AUTOSAR element."""

from typing import Optional, cast
import xml.etree.ElementTree as ET
from armodel.models.M2.AUTOSARTemplates.CommonStructure.Implementation.implementation import (
    Implementation,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Identifier,
    RevisionLabelString,
)
from armodel.models.M2.AUTOSARTemplates.BswModuleTemplate.BswBehavior.bsw_internal_behavior import (
    BswInternalBehavior,
)
from armodel.models.M2.AUTOSARTemplates.ECUCParameterDefTemplate.ecuc_module_def import (
    EcucModuleDef,
)


class BswImplementation(Implementation):
    """AUTOSAR BswImplementation."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: (member_name, xml_tag_name, is_attribute, is_list, element_class)
    _xml_members = [
        ("ar_release", None, True, False, None),  # arRelease
        ("behavior", None, False, False, BswInternalBehavior),  # behavior
        ("preconfigureds", None, False, True, any (EcucModule)),  # preconfigureds
        ("recommendeds", None, False, True, any (EcucModule)),  # recommendeds
        ("vendor_api_infix", None, True, False, None),  # vendorApiInfix
        ("vendor_specifics", None, False, True, EcucModuleDef),  # vendorSpecifics
    ]

    def __init__(self) -> None:
        """Initialize BswImplementation."""
        super().__init__()
        self.ar_release: Optional[RevisionLabelString] = None
        self.behavior: Optional[BswInternalBehavior] = None
        self.preconfigureds: list[Any] = []
        self.recommendeds: list[Any] = []
        self.vendor_api_infix: Optional[Identifier] = None
        self.vendor_specifics: list[EcucModuleDef] = []

    def serialize(self, namespace: str, element: Optional[ET.Element] = None) -> ET.Element:
        """Convert BswImplementation to XML element.

        Args:
            namespace: XML namespace for the element
            element: Optional existing element to add members to (for subclass chaining)

        Returns:
            XML element representing this object
        """
        # ARObject.serialize() handles entire class hierarchy automatically
        return super().serialize(namespace, element)

    @classmethod
    def deserialize(cls, element: ET.Element) -> "BswImplementation":
        """Create BswImplementation from XML element.

        Args:
            element: XML element to deserialize from

        Returns:
            BswImplementation instance
        """
        # ARObject.deserialize() handles entire class hierarchy automatically
        obj = super().deserialize(element)
        # Cast to BswImplementation since parent returns ARObject
        return cast("BswImplementation", obj)


class BswImplementationBuilder:
    """Builder for BswImplementation."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: BswImplementation = BswImplementation()

    def build(self) -> BswImplementation:
        """Build and return BswImplementation object.

        Returns:
            BswImplementation instance
        """
        # TODO: Add validation
        return self._obj
