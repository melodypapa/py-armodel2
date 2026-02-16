"""RPortPrototype AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.Components.abstract_required_port_prototype import (
    AbstractRequiredPortPrototype,
)
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    Boolean,
)
from armodel.models.M2.AUTOSARTemplates.SWComponentTemplate.PortInterface.port_interface import (
    PortInterface,
)


class RPortPrototype(AbstractRequiredPortPrototype):
    """AUTOSAR RPortPrototype."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "may_be": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # mayBe
        "required": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=PortInterface,
        ),  # required
    }

    def __init__(self) -> None:
        """Initialize RPortPrototype."""
        super().__init__()
        self.may_be: Optional[Boolean] = None
        self.required: Optional[PortInterface] = None


class RPortPrototypeBuilder:
    """Builder for RPortPrototype."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: RPortPrototype = RPortPrototype()

    def build(self) -> RPortPrototype:
        """Build and return RPortPrototype object.

        Returns:
            RPortPrototype instance
        """
        # TODO: Add validation
        return self._obj
