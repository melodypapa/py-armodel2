"""LinConfigurableFrame AUTOSAR element."""

from typing import Optional
import xml.etree.ElementTree as ET
from armodel.serialization import XMLMember

from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.ar_object import ARObject
from armodel.models.M2.AUTOSARTemplates.GenericStructure.GeneralTemplateClasses.PrimitiveTypes import (
    PositiveInteger,
)
from armodel.models.M2.AUTOSARTemplates.SystemTemplate.Fibex.Fibex4Lin.LinCommunication.lin_frame import (
    LinFrame,
)


class LinConfigurableFrame(ARObject):
    """AUTOSAR LinConfigurableFrame."""

    # XML member definitions for this class only (not inherited from parent classes)
    # Format: dict[str, XMLMember] for declarative metadata
    _xml_members: dict[str, "XMLMember"] = {
        "frame": XMLMember(
            xml_tag=None,
            is_attribute=False,
            multiplicity="0..1",
            element_class=LinFrame,
        ),  # frame
        "message_id": XMLMember(
            xml_tag=None,
            is_attribute=True,
            multiplicity="0..1",
        ),  # messageId
    }

    def __init__(self) -> None:
        """Initialize LinConfigurableFrame."""
        super().__init__()
        self.frame: Optional[LinFrame] = None
        self.message_id: Optional[PositiveInteger] = None


class LinConfigurableFrameBuilder:
    """Builder for LinConfigurableFrame."""

    def __init__(self) -> None:
        """Initialize builder."""
        self._obj: LinConfigurableFrame = LinConfigurableFrame()

    def build(self) -> LinConfigurableFrame:
        """Build and return LinConfigurableFrame object.

        Returns:
            LinConfigurableFrame instance
        """
        # TODO: Add validation
        return self._obj
