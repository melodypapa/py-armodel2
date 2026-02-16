"""RtePluginProps AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.ECUCDescriptionTemplate.ecuc_container_value import (
    EcucContainerValue,
)


class RtePluginProps(ARObject):
    """AUTOSAR RtePluginProps."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "associated": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcucContainerValue,
        ),  # associated
        "associated_rte": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=EcucContainerValue,
        ),  # associatedRte
    }

    def __init__(self) -> None:
        """Initialize RtePluginProps."""
        super().__init__()
        self.associated: Optional[EcucContainerValue] = None
        self.associated_rte: Optional[EcucContainerValue] = None


class RtePluginPropsBuilder:
    """Builder for RtePluginProps."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RtePluginProps = RtePluginProps()

    def build(self) -> RtePluginProps:
        """Build and return RtePluginProps object.

        Returns:
            RtePluginProps instance
        """
        # TODO: Add validation
        return self._obj
